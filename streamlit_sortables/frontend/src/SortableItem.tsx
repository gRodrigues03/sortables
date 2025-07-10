import React, { ReactNode, FunctionComponent, useState } from 'react';
import { useSortable } from '@dnd-kit/sortable';
import { CSS } from '@dnd-kit/utilities';

import './SortableComponent.css';


type AvailableColorProps = { [name: string]: string };

export interface SortableItemProps {
  id: string,
  ghost: boolean,
  onColorChange?: (color: string) => void,
  onContextMenuChange?: () => void,
  isActive?: boolean,
  children?: ReactNode,
  isOverlay?: boolean,
  color?: string,
  availableColors?: AvailableColorProps[]
}

export const SortableItem: FunctionComponent<SortableItemProps> = ((props) => {
  const {
    attributes,
    listeners,
    setNodeRef,
    transform,
    transition
  } = useSortable({ id: props.id });

  const sortableProps = props.isOverlay ? {
    attributes: {},
    listeners: {},
    setNodeRef: null,
    transform: null,
    transition: undefined,
    isDragging: true
  } : {
    attributes,
    listeners,
    setNodeRef,
    transform,
    transition,
    isDragging: false
  };

  const availableColors = props.availableColors ?? [];
  const [contextMenuVisible, setContextMenuVisible] = useState(false);
  const [contextMenuPos, setContextMenuPos] = useState<{ x: number, y: number }>({ x: 0, y: 0 });
  const [itemColor, setItemColor] = useState<string>("");

  const handleContextMenu = (e: React.MouseEvent) => {
    e.preventDefault();
    setContextMenuPos({ x: e.clientX, y: e.clientY });
    setContextMenuVisible(true);
    props.onContextMenuChange?.();
  };

  const handleColorChange = (color: string) => {
    props.onColorChange?.(color);
    setContextMenuVisible(false);
    props.onContextMenuChange?.();
  };

  const handleClickAnywhere = () => {
    setContextMenuVisible(false);
    props.onContextMenuChange?.();
  };

  const handleOtherRightClick = (e: MouseEvent) => {
    if (e.button === 2) {
        setContextMenuVisible(false);
        props.onContextMenuChange?.();
    }

  };

  React.useEffect(() => {
    window.addEventListener("click", handleClickAnywhere);
    window.addEventListener("mousedown", handleOtherRightClick);
    return () => window.removeEventListener("click", handleClickAnywhere);
  }, []);

  const style: React.CSSProperties = {
    transform: sortableProps.transform ? CSS.Transform.toString(sortableProps.transform) : undefined,
    transition: sortableProps.transition,
    cursor: sortableProps.isDragging ? 'grabbing' : 'grab',
    backgroundColor: props.color || ""
  };

  const className = `btn shadow-none sortable-item ${props.isActive ? "active" : ""} ${sortableProps.isDragging ? "dragging" : ""}`;
    if (!props.ghost) {
  return (
    <>
      <li
        className={className}
        data-testid={props.children ? props.children : null}
        ref={sortableProps.setNodeRef}
        style={style}
        onContextMenu={handleContextMenu}
        {...sortableProps.attributes}
        {...sortableProps.listeners}
      >
        {props.children ? props.children : null}
      </li>

      {contextMenuVisible && (
        <ul
          className="context-menu"
          style={{
            position: 'fixed',
            top: contextMenuPos.y,
            left: contextMenuPos.x,
            listStyle: 'none',
            zIndex: 1000
          }}
        >
          {availableColors.map((colorObj) => {
  const [name, value] = Object.entries(colorObj)[0];
  return (
    <li key={value} onClick={() => handleColorChange(value)}>
      {name}
    </li>
  );
})}
          <li onClick={() => handleColorChange('')}>Resetar</li>
        </ul>
      )}
    </>
  );
  } else {
      return (
    <>
      <li
        className={className}
        data-testid={props.children ? props.children : null}
        ref={sortableProps.setNodeRef}
        style={style}
        {...sortableProps.attributes}
        {...sortableProps.listeners}
      >
        {props.children ? props.children : null}
      </li>
    </>
  );
      }
});

