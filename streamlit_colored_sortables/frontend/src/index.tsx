import React from "react";
import ReactDOM from "react-dom";
import SortableComponentWrapper from "./SortableComponent";


const observerError = 'ResizeObserver loop completed with undelivered notifications';
const originalError = window.onerror;
window.onerror = function(message, source, lineno, colno, error) {
  if (typeof message === 'string' && message.includes(observerError)) {
    return true; // Suprime
  }
  return originalError?.(message, source, lineno, colno, error);
};

ReactDOM.render(
    <SortableComponentWrapper />,
    document.getElementById("root")
);
