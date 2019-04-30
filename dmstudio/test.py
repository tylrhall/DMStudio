from dmstudio import dmcommands
from dmstudio import special
from dmstudio import dmfiles
from dmstudio import dmdir as f

print f.file




cmd = dmcommands.studio(version='StudioEM')
cmd.copy(in_i='fake_model', out_o='fake_model_copy', retrieval='AU>2.0')

print('success')