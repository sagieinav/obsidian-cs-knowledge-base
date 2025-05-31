<%*
const selectedText = tp.editor.selection;

if (selectedText) {
    // Wrap the selected text with ==** and **==
    tp.editor.replaceSelection('==**' + selectedText + '**==');
} else {
    // If no text is selected, insert ==****== and place the cursor in the middle
    tp.editor.replaceSelection('==****==');
    // Move cursor back 3 characters to be between the bold markers
    tp.editor.cursor.moveBy(-3);
}
%>
