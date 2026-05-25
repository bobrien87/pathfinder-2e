---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Divine]]", "[[Versatile p]]"]
price: "{'gp': 2000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When a once-in-a-lifetime alignment of the stars shone through the roof of a secluded blacksmith's forge, the smith took advantage to craft their masterpiece. For two hours, they hammered a lump of ordinary steel into a divine blade, etching constellations and wards down its length, then shared their creation's formula with a small group of close associates before passing away.

These weapons are the four-tiger blades, and currently, only a dozen are known to exist—one associated with each month of the year. Each weapon is a *+2 striking ghost touch longsword* that leaves a noticeable trail of light originating from the engraved stars when it's swung. Those who pay close attention to the pattern of stars that shine on the blade might note that the depicted constellations change according to those currently in the night sky above.

**Activate—Ghost Blocking Tiger** `pf2:r` (concentrate)

**Trigger** You attempt a Strike with the four-tiger-blade

**Effect** Until the start of your next turn, you gain void resistance 10.

> [!danger] Effect: Four Tiger Blade

**Activate—Ghost Chasing Tiger** `pf2:2` (concentrate, divine, incapacitation, manipulate)

**Frequency** once per day

**Effect** Attempt a Strike against a creature you believe to be possessed. This attack deals no damage to the creature, but if the target is possessed, the possessing creature must attempt a DC 29 [[Will]] save.
- **Critical Success** The possessing creature is unaffected, and you remain unaware of if the target is actually possessed or not.
- **Success** The possessing creature is unaffected, but you sense that creature's control over the target and confirm that the target is possessed.
- **Failure** You confirm that the target is possessed. The possessing creature can't control the target for 1 minute.
- **Critical Failure** You confirm the target is possessed an instant before you automatically counteract the possession, causing the possessing creature to vacate the target's body.

**Source:** `= this.source` (`= this.source-type`)
