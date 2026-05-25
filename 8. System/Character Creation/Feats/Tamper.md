---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Inventor]]", "[[Manipulate]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You tamper with a foe's weapon or armor, using a free hand. Choose either a weapon held by an enemy in your reach or a suit of armor worn by an enemy in your reach. Attempt a [[Crafting]] check against the enemy's Reflex DC.
- **Critical Success** Your tampering is incredibly effective. If you tampered with a weapon, the enemy takes a -2 circumstance penalty to attack rolls and damage rolls with that weapon. If you tampered with armor, the armor hampers the enemy's movement, making the enemy [[Off Guard]] and inflicting a –10-foot penalty to its Speeds. The effect lasts until the enemy Interacts to remove it, regardless of which one you used. 

> [!danger] Effect: Armor Tampered With (Critical Success)

 

> [!danger] Effect: Weapon Tampered With (Critical Success)
- **Success** Your tampering is temporarily effective. As critical success, but the effect ends at the start of your next turn, even if the enemy doesn't Interact to end it. 

> [!danger] Effect: Armor Tampered With (Success)

 

> [!danger] Effect: Weapon Tampered With (Success)
- **Critical Failure** Your tampering backfires dramatically, creating a small explosion from your own tools or gear. You take @Damage[(@actor.level)[fire]]{fire damage equal to your level}.

**Source:** `= this.source` (`= this.source-type`)
