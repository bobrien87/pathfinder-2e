---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Concentrate]]", "[[Incarnate]]", "[[Manipulate]]", "[[Mythic]]"]
cast: "`pf2:3`"
range: "100 feet"
duration: "until the end of your next turn"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

With a whispered prayer or arcane sending, you conjure Arcanotheign, herald of Nethys. She's a storm of magic, half white and half black, roiling in a vaguely humanoid shape. She occupies the space of a Medium creature and has a Speed of 40 feet and a fly Speed of 60 feet.

**Arrive** (sonic) *Storm's Unbridled Destruction* Arcanotheign arrives with a flash of light and a cacophonous crash of colliding magic. All enemies in a @Template[type:emanation|distance:60] take 8d12 sonic damage with a basic Reflex save. A creature that critically fails is additionally [[Deafened]] for 10 minutes.

**Depart** (electricity, healing) *Flash of Brilliance* Arcanotheign fires a powerful arcane blast at one target within 100 feet, dealing 5d12 electricity damage with a basic Reflex save, and a powerful divine blast at one ally, healing 5d12 Hit Points. Then, Arcanotheign asks for payment in the form of a fond memory. If you pay this cost, you lose this memory, Arcanotheign gains this memory, and Arcanotheign whispers a secret into your mind; you can immediately [[Recall Knowledge]] on any subject at mythic proficiency.

**Source:** `= this.source` (`= this.source-type`)
