---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Divine]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 300}"
usage: "worn"
bulk: "—"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This strand of charms depicts the legendary harpy Ekriathe and her six reincarnated successors. Each charm can be removed and activated. When all of the charms are consumed, the strand becomes inert.

**Activate—Hero-God's Whisper** `pf2:2` (auditory, interact, light)

**Effect** You detach a charm, which creates a glowing ghostly image of the hero-god depicted on it. This image sheds bright light in a 20-foot radius (and dim light for the next 20 feet) for 1 hour. Allies within the image's bright light hear the constant whispers of Ekriathe or her successor's voice, and they gain a +2 status bonus to saving throws against auditory effects. Enemies entering or ending their term in the image's radius of bright light must attempt a DC 23 [[Will]] save. On a failure, the target is [[Fascinated]] and takes a –2 status penalty to auditory-based Perception checks while they remain in the radius. Creatures that succeed against this effect are temporarily immune for the next 24 hours.

**Source:** `= this.source` (`= this.source-type`)
