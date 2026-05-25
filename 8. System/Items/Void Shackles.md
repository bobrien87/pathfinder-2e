---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Magical]]", "[[Void]]"]
price: "{'gp': 12500}"
usage: "held-in-two-hands"
bulk: "—"
source: "Pathfinder #212: A Voice in the Blight"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

*Void shackles* are built from supernatural crystals that form in the Void—materials that dig painfully into the flesh of those they restrain. A set of *void shackles* functions as superior manacles, but while they are in the Void, the crystals fluctuate in response to the plane's energy, which increases all DCs to remove them or [[Escape]] by 1 to DC 43. If a check to remove *void shackles* from a creature fails, the wearer of the manacles takes 10d6 void damage (DC 37 [[Fortitude]] save). While a creature is manacled, the *void shackles* attempt to counteract any teleportation effect that targets the manacled creature, with a counteract rank of 9th and a +25 modifier to the roll. If the teleportation effect is countered, the manacled creature takes 10d6 void damage (DC 37 [[Fortitude]] save).

Void shackles can be placed on incorporeal creatures as if they were not incorporeal. An incorporeal creature manacled by *void shackles* cannot pass through solid objects. Even a soul can be [[Restrained]] via *void shackles*, provided the soul was of a 17th- or lower-level creature in life. A soul held in *void shackles* cannot move on to the afterlife, cannot become undead, and can be transported by simply transporting the shackles.

**Activate—Affix Shackle** `pf2:2` (manipulate)

**Effect** You affix the *void shackles* to a helpless or willing creature or to any 17th- or lower-level soul. The shackles grow in size to accommodate the wrists or ankles of any size creature.

**Activate—Release Shackle** `pf2:2` (manipulate)

**Effect** You cause the *void shackles* to open and release their prisoner. If you were not the one to affix the shackles to that creature or soul, you must attempt a DC 43 [[Will]] save.
- **Critical Success** The shackles open.
- **Success** The shackles open, but you and the shackled creature take 5d6 void damage.
- **Failure** The shackles do not open, and you and the shackled creature take 10d6 void damage.
- **Critical Failure** As failure, but 20d6 void damage.

**Source:** `= this.source` (`= this.source-type`)
