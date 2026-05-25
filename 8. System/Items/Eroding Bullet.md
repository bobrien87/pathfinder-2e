---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Acid]]", "[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 22}"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** round

**Activate** `pf2:1` (manipulate)

Eroding bullets cast a faint green glow, and smell like the sickly- sweet organic gases that rise from corpses. Handling an eroding bullet without gloves deals 1 acid damage and leaves the putrid scent coated on your fingers. Upon Striking an enemy, the glass casing inside the bullet bursts, releasing a splattering of bubbling green acid that coats the target. The target takes 2d6 persistent,acid damage in addition to the damage normally dealt by the attack.

**Source:** `= this.source` (`= this.source-type`)
