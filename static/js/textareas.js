$(document).ready(function() 
{ tinymce.DOM.addClass (tinymce.DOM.select('.edit .vLargeTextField'), 'mcEdit');

  tinyMCE.init({
    mode : "textareas",
    theme : "advanced",
    editor_selector : "mcEdit",  // doesn't support selectors, only classes, despite the name
    height: "480",
    width: "90%",
    element_format : "html",
    plugins : "preview,fullscreen",
    theme_advanced_buttons3_add : "preview,fullscreen",
    theme_advanced_toolbar_location : "top",
    theme_advanced_toolbar_align : "left",
    theme_advanced_statusbar_location : "bottom",
    //theme_advanced_resizing : true,
  });
});
