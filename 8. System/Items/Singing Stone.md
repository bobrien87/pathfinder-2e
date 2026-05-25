---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Earth]]", "[[Magical]]"]
price: "{'gp': 3000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *singing stone* looks like a drinking cup made of polished rock, and it always faintly hums or keens. Anyone who carries the cup for some time senses that it changes its tune depending on the types of rock nearby and that it grows quiet in areas with little stone. A *singing stone* is a planar key for [[Interplanar Teleport]] and similar magic. When it's used this way, you're more likely to arrive where you intend to be, appearing 1d6×25 miles from your intended destination instead of 1d10×25 miles away.

**Activate—Stone's Speech** 1 minute (manipulate)

**Frequency** once per day

**Effect** The *singing stone* casts *speak with stones*, allowing you to speak and listen through the bowl to communicate with stones. You can use the spell normally, or, as you activate the *singing stone*, you can target one stone you can clearly identify in appearance and location. This target must be on the same plane as you or on the Plane of Earth. You can't change targets during a single activation.

**Activate—Stone's Sight** `pf2:1` (manipulate, revelation)

**Frequency** once per day

**Effect** Placing the *singing stone* against a rocky surface, you cause it to reverberate, revealing what's behind or beneath the surface. You get a mental image of this area that's 15 feet deep and 5 feet in diameter. The image doesn't convey color, but it's clear to you what objects or creatures within are moving and which are stationary. The image is instant, however, and therefore doesn't allow you to track movement over time.

**Source:** `= this.source` (`= this.source-type`)
