---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]", "[[Razing]]", "[[Shove]]", "[[Two hand d10]]", "[[Versatile p]]"]
price: "{'gp': 250}"
usage: "held-in-one-hand"
bulk: "2"
source: "Pathfinder #208: Hoof, Cinder, and Storm"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The steel head of this *+1 striking earthbreaker* has a large crack that zigzags down its center, making it look like it could crack in half with any swing. This belies the hammer's strength; its strikes can shatter stone with ease.

**Activate—Create Faultline** `pf2:f` (concentrate)

**Frequency** once per day

**Trigger** You Strike an object or raised shield with the faultline hammer and would deal piercing damage to that object

**Effect** Until the end of your next turn, any weapon that Strikes the object deals additional damage as though the weapon had the razing trait. The triggering Strike also deals this additional damage.

**Source:** `= this.source` (`= this.source-type`)
