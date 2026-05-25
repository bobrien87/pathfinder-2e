---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Apex]]", "[[Artifact]]", "[[Flexible]]", "[[Intelligent]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
bulk: "L"
source: "Pathfinder #212: A Voice in the Blight"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +34; precise low-light vision and hearing within 30 feet

**Communication** telepathy (partner only)

**Skills** Intimidation +35, Society +33, Warfare +33

**Int** +5, **Wis** +6, **Cha** +7

**Will** +34

The heroism of Kyloss Syndar, founder of Greengold and slayer of the demonic hydra Slithermaw, imprinted this suit of armor with a gleaming, prismatic sheen that sparkles under bright light. The telepathic voice of *Slithermaw's Bane* is boisterous and grandiose, encouraging his partner to take up leadership roles while also providing advice to maintain loyalty and strengthen bonds of friendship.

*Slithermaw's Bane* is a suit of *+3 major resilient greater fortification high-grade elven chain* that grants his wearer poison resistance 15, and the item bonus this resilient rune grants to saving throws versus poison increases by 1 to +4.

**Activate—Calistria's Sting** `pf2:r` (concentrate, poison)

**Frequency** once per day

**Trigger** A creature grapples you

**Effect** Poison wells up from the armor's links to seep into the triggering creature's body, causing it to suffer wracking pains as if it was being stung by thousands of angry wasps. The triggering creature takes 7d6 persistent,poison damage (DC 34 [[Fortitude]] save); this persistent damage can't be ended as long as the triggering creature continues to grapple you. *Slithermaw's Bane* can't activate Calistria's Sting using his actions.

**Activate—Purge Toxins** `pf2:2` (concentrate)

**Frequency** once per minute

**Effect** *Slithermaw's Bane* attempts to counteract a disease or poison affliction affecting you, with a counteract rank of 9th and a +25 modifier to the roll (+30 modifier if the source of the disease or poison effect on you was created by a fiend).

**Activate—Terrain Adaptation** `pf2:2` (concentrate)

**Frequency** once per hour

**Effect** You alter the exterior of the armor to better adapt to the surrounding terrain: aquatic, arctic, desert, forest, mountain, plains, sky, swamp, or underground. You ignore difficult terrain within the chosen environment and gain a +2 circumstance bonus to saving throws against environmental hazards, natural disasters, and extreme temperatures that originate from that terrain. You're also protected from severe and extreme heat or severe and extreme cold (your choice when you activate this ability). This effect lasts until your next daily preparations or the next time you activate it, whichever comes first.

**Source:** `= this.source` (`= this.source-type`)
