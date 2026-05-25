---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]"]
price: "{'gp': 675}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This net was woven by the jorogumo Injigo, who presented it as a gift to her gnome sweetheart, Mara, to keep her safe in their mountain cottage whenever Injigo left home to go on hunting expeditions.

*Injigo's Loving Embrace* functions as a typical net. You gain a +1 item bonus to Athletics checks to [[Grapple]] with the net.

**Activate—Ensnare Ghost** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You spin the net in the direction of an incorporeal creature within 30 feet that you can see. Lines of silken force whip out to lash around the incorporeal creature, who must succeed at a DC 25 [[Reflex]] save or become [[Immobilized]] until the end of your next turn. You can Sustain this activation for up to 1 minute, and the creature must succeed at a DC 25 check to [[Escape]] the net.

**Activate—A Night of Melancholic Dreams** 10 minutes (concentrate, manipulate)

**Frequency** once per week

**Effect** You wrap the net around you like a blanket as you prepare to sleep. As long as you get 8 hours of sleep or analogous rest, you dream of writing love letters to someone you adore: this could be an actual paramour, someone you're interested in, or someone unknown whose identity you don't recall after waking. When you wake, you're filled with a sense of melancholia about those unsent letters, but these feelings distract you from other, more unpleasant thoughts, granting you mental resistance 5 and a +1 item bonus to saving throws against mental effects for the next 8 hours.

> [!danger] Effect: Injigo's Loving Embrace

**Source:** `= this.source` (`= this.source-type`)
