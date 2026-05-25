---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Cursed]]", "[[Magical]]", "[[Scrying]]"]
price: "{'gp': 3800}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A tattletale orb is a polished crystal sphere that appears to function as a [[Crystal Ball (Clear Quartz)]]. If those whom you use the orb to scry on roll better than a critical failure on their saving throw, they receive a telepathic message alerting them to the scrying. A success or better at the save allows the target to choose to allow you to scry anyway, knowing they can use an aspect of the orb against you, according to the orb's type. A creature that rolls a critical success on the saving throw also learns your name and location. Once you Activate a tattletale orb or use it to cast one of your scrying spells, it fuses to you. You must succeed at a Will save, using the scrying Will DC of a crystal ball of the orb's type, to use another such device.

Tattletale orbs come in the same types as crystal balls, with the same activations and powers. However, your target must roll a critical failure on the saving throw for the orb to function as normal for that type of crystal ball.

**Source:** `= this.source` (`= this.source-type`)
