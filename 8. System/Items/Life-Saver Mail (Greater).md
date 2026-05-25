---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Magical]]"]
price: "{'gp': 52500}"
bulk: "3"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This suit of *+3 greater resilient greater fortification splint mail* has a large, green gemstone inset in a prominent location. While wearing the armor, you feel at ease knowing the armor can protect you in even dire circumstances. The gemstone glows with life essence, casting green light as brightly as a torch. You can suppress or resume this light by using a single action, which has the concentrate trait.

**Activate—Second Chance** R (concentration)

**Frequency** once per day

**Trigger** You would die

**Effect** The armor's gemstone turns gray as it shares life energy with you. The armor casts [[Breath of Life]] on you.

**Activate—Shielding Light** `pf2:2` (concentration, manipulate)

**Effect** You tap on the gemstone, producing a protective screen of green light. You cast a 9th-rank [[Shield]] spell. As normal with the spell, you can't cast *shield* again (using this activation or other means) for 10 minutes if you use it to Shield Block.

**Source:** `= this.source` (`= this.source-type`)
