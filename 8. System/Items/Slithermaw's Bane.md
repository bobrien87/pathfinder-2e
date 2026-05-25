---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Flexible]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 6500}"
bulk: "L"
source: "Pathfinder #211: The Secret of Deathstalk Tower"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This suit of *+2 greater resilient elven chain* was worn by the elven hero Kyloss Syndar. The armor served him well, but eventually he fell in battle against the demonic hydra Slithermaw. As Kyloss slew the demonic beast, its fangs pierced his chest and mortally wounded the elf. The armor retains several ragged holes along the chest and abdomen where the hydra's teeth damaged it.

*Slithermaw's Bane* grants its wearer poison resistance 10, and the resilient rune increases the item bonus on saving throws versus poison by 1 (to +3).

**Activate—Calistria's Sting** `pf2:r` (concentrate, divine)

**Frequency** once per day

**Trigger** A creature grapples you

**Effect** Poison wells up from the armor's links to seep into the triggering creature's body, causing it to suffer wracking pains as if it were being stung by thousands of angry wasps. The triggering creature takes 7d6 persistent,poison damage (DC 34 [[Fortitude]] save); this persistent damage cannot be ended as long as the triggering creature continues to grapple you.

**Activate—Terrain Adaptation** 10 minutes (concentrate, divine)

**Frequency** once per day

**Effect** You alter the exterior of the armor to better adapt to the surrounding terrain: aquatic, arctic, desert, forest, mountain, plains, sky, swamp, or underground. You ignore non-magical difficult terrain within the chosen environment and gain a +1 circumstance bonus to saving throws against environmental hazards, natural disasters, and extreme temperatures that originate from that terrain. You are also protected from severe and extreme heat or severe and extreme cold (your choice when you activate this ability). This effect lasts until your next daily preparation.

**Source:** `= this.source` (`= this.source-type`)
