---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Artifact]]", "[[Divine]]"]
price: "{'value': {}}"
usage: "worn"
bulk: "L"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These nine flawless gems are set within a golden necklace, their centerpiece a holy ruby pulled from the center of a sun. So long as you are wearing the navaratna, you ignore all environmental effects due to temperature, do not take penalties due to wind, and ignore all damage and effects from droughts, floods, and earthquakes. You are also immune to damage from starvation. The navaratna does not otherwise grant you resistance against damage (such as fire or cold damage).

**Activate—Sutra of the Flawless Servant** `pf2:r` (concentrate, divine, fortune)

**Frequency** once per hour

**Trigger** An ally within 30 feet fails a saving throw against an environmental effect or a spell with the air, earth, fire, or water trait

**Effect** You offer a prayer for your divine protection to extend to your companion. The creature rerolls the triggering saving throw with a +2 item bonus. They must take the new result, even if it is worse.

**Destruction** The navaratna must be swallowed by a fiendish divine lion; the lion must then by killed by drowning in a lake of naga venom and left to rot for a year. At the stroke of midnight on the final day, the artifact is destroyed.

**Source:** `= this.source` (`= this.source-type`)
