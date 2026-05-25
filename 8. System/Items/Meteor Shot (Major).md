---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Consumable]]", "[[Fire]]", "[[Magical]]", "[[Splash]]"]
price: "{'gp': 3000}"
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

This craggy stone ammunition is warm to the touch. When you fire an activated meteor shot, it explodes into a small swarm of meteors as it reaches its target, scorching nearby creatures and littering the ground with rubble. In addition to the weapon's normal damage, the meteor shot deals fire damage and the ground in the area becomes difficult terrain.

The ammunition deals @Damage[9d6[fire]|options:area-damage] damage in a @Template[emanation|distance:20] around the target (DC 37 [[Reflex]] save).

In addition, the Strike gains the following critical failure effect.
- **Critical Failure** The weapon misfires.

**Source:** `= this.source` (`= this.source-type`)
