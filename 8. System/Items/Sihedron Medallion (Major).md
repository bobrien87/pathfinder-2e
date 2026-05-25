---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 6500}"
usage: "worn"
bulk: "—"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These amulets once served as tokens of loyalty between the runelords and their favored agents. Though they vary in appearance, they all share a common design—a leather or metallic cord attached to a metal disc inscribed with the seven-pointed star known as the Sihedron. For original *Sihedron medallions* created before Earthfall, a runelord of old Thassilon (not a character with the runelord archetype) doesn't reduce the DC of any [[Scrying]] spell they cast against a creature that wears a *Sihedron medallion* even if they have never met the target or are unaware of the target's identity. If such a runelord successfully scries on a creature wearing an original *Sihedron medallion*, they can use the wearer's voice to issue messages to those in the vicinity. *Sihedron medallions* created in more modern times don't possess this disadvantage.

A dead body that wears a *Sihedron medallion* doesn't decay, and bugs or other pests (such as maggots) are prevented from consuming the remains, but unlike the effects of [[Peaceful Rest]], this doesn't offer any protection against undeath, nor does it have an impact on spells that require the corpse to have died within a certain amount of time.

**Activate—Bolster Flesh** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** Your flesh is augmented with magical vitality. You gain a +2 item bonus to saving throws and 25 temporary Hit Points for 8 hours.

> [!danger] Effect: Bolster Flesh

**Source:** `= this.source` (`= this.source-type`)
