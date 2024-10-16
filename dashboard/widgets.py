from django.forms import ClearableFileInput
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

class ImageUploadWidget(ClearableFileInput):
    template_name = 'widgets/image_upload_widget.html'
    
    def __init__(self, attrs=None):
        default_attrs = {'class': 'custom-file-input'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

    def format_value(self, value):
        if value and hasattr(value, 'url'):
            return mark_safe(f'''
                <div id="image-upload" class="text-center">
                    <img src="{value.url}" alt="Product Image" id="product-image" style="width: 140px; border-radius: 5px;"/>
                    <div id="upload-icon" class="text-center">
                        <label for="id_image">
                            <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
                              <path fill-rule="evenodd" d="M12 3a1 1 0 0 1 .78.375l4 5a1 1 0 1 1-1.56 1.25L13 6.85V14a1 1 0 1 1-2 0V6.85L8.78 9.626a1 1 0 1 1-1.56-1.25l4-5A1 1 0 0 1 12 3ZM9 14v-1H5a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2h-4v1a3 3 0 1 1-6 0Zm8 2a1 1 0 1 0 0 2h.01a1 1 0 1 0 0-2H17Z" clip-rule="evenodd" />
                            </svg>
                        </label>
                        <input type="file" id="id_image" name="image" class="d-none" />
                    </div>
                </div>
            ''')
        return super().format_value(value)
