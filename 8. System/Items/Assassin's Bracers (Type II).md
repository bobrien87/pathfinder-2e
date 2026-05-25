---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Illusion]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 6500}"
usage: "wornbracers"
bulk: "L"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These paired bracers of red leather appear as plain armbands on the outside but display the branded symbol of [[Achaekek]] on the inside. They grant the wearer a +2 item bonus to AC and saving throws, and a maximum Dexterity modifier of +5 as armor. You can affix talismans to *assassin's bracers* as though they were light armor.

**Activate—Focus on the Doomed** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You designate one creature within 30 feet. You cast 4th-rank [[Invisibility]] on yourself, but the designated creature can still see you. The bracers enhance your appearance to the designated creature, making you appear more fearsome and unnerving, granting you a +2 item bonus to attempts to [[Feint]] or [[Demoralize]] the designated creature. The designated creature takes a –2 item penalty to saving throws against fear effects.

> [!danger] Effect: Focus on the Doomed

> [!danger] Effect: Focus on the Doomed (Fear Penalty)

**Source:** `= this.source` (`= this.source-type`)
