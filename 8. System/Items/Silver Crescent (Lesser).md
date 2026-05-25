---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Light]]", "[[Lozenge]]"]
price: "{'gp': 35}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A piquant tamarind and chili-lime flavor infuses a silver crescent, which was first created to aid those battling the undead. For 1 hour, you shed cool, white light like a torch, and you gain a +1 item bonus to saving throws against olfactory effects. While shedding this light, you can't be [[Concealed]] if you're visible, and if you're [[Invisible]], you're concealed instead rather than being undetected.

> [!danger] Effect: Silver Crescent

**Secondary Effect** `pf2:2`

**Effect** A ray of light descends on a 5-foot square of your choice within 120 feet. Any creature in that space takes @Damage[4d6[vitality]|options:area-damage] with a DC 20 [[Reflex]] save and is [[Dazzled]] until the end of its next turn on a failed save. This is treated as silver for the purposes of weaknesses, resistances, and the like. The silver crescent becomes inert.

**Source:** `= this.source` (`= this.source-type`)
