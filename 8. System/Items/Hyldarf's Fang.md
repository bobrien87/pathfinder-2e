---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Modular]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 greater striking hand cannon* is carved and crafted from a single large fang, worn with age and cracked with red lines. The tip of the fang has been filed down, but still leaks black fluid occasionally. It was fashioned from the tooth of the tor linnorm Hyldarf by a half-Ulfen gunsmith from Tian Xia who sought the title of linnorm king. Though the smith failed to slay the linnorm, he did claim the mighty dragon's tooth and fashion it into a magic firearm that still drips warm venom. Hyldarf survived the encounter with her attacker and slew the gunsmith years later, though by then the smith had already bequeathed the weapon to his chosen heir and it was far out of her grasp. The linnorm still searches for her missing tooth, portending potential doom for the weapon's owner.

The weapon deals an additional 2d6 fire damage on a successful Strike, plus 3d10 persistent,fire damage on a critical hit. Fire damage dealt by this weapon (including persistent fire damage and damage from Hyldarf's Venom) ignores the target's fire resistance.

**Activate—King of Linnorms** `pf2:3` (manipulate)

**Frequency** once per day

**Effect** You call upon Hyldarf's power to gain the magic of a linnorm for a brief time. For 1 minute, you gain the effects of fly, unfettered movement, and truesight as well as fire resistance 20.

> [!danger] Effect: Hyldarf's Fang

**Activate—Linnorm's Fang** `pf2:1` (manipulate)

**Frequency** Once per minute

**Effect** You soak your shot in the fluid of the fang, imbuing it with Hyldarf's venom. The next Strike you make with Hyldarf's Fang before the end of your next turn delivers the venom to the target.

**Hyldarf's Venom** (fire, injury, poison)

**Saving Throw** DC 34

**Maximum Duration** 3 rounds

**Stage 1** 3d6 fire damage and [[Sickened]] 1

**Stage 2** 6d6 fire damage and [[Sickened]] 2.

**Source:** `= this.source` (`= this.source-type`)
