import obd

controller = obd.OBD()

cmd = obd.commands.SPEED

response = controller.query(cmd)

print(response.value)
print(response.value.to('mph'))

