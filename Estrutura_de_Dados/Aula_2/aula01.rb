lista = []

puts <<~MENU
       Menu de Opções:
       1-Para adicionar um número:
       2-Para excluir o primeiro elemento:
       3-Para excluir o último elemento:
       4-Para adicionar um número em primeiro lugar:
       5-Para mostrar a lista (array):
       6-Para excluir os números ímpares:
       7-Para excluir os números pares:
       0-Para sair:
MENU

loop do
  puts "informe a opção:"
  opc = gets.to_i

  case opc
  when 1
    puts "Informe o numero:"
    num = gets.to_i
    lista << num
  when 2
    lista.shift
  when 3
    lista.pop
  when 4
    puts "Informe o numero para por em primeiro lugar:"
    num = gets.to_i
    lista.unshift(num)
  when 5
    puts "Os numeros são:"
    puts lista
  when 6
    lista.delete_if { |item| item.odd? }
  when 7
    lista.delete_if { |item| item.even? }
  when 0
    break
  else
    puts 'Opção incorreta!! Informe um número válido!!'
  end
end