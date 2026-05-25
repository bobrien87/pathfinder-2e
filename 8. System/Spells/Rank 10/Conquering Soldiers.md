---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "10"
traits: ["[[Concentrate]]", "[[Incarnate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "500 feet"
duration: "until the end of your next turn"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You tap into the glories of the armies of old, bringing forth their might to your battlefield and making their strength and power your own. This army manifests as glimmering forms of a conquering military of old, replete with banners and colors of their nation. The army occupies the space of a Gargantuan creature and has a Speed of 80 feet.

**Arrive** (auditory, emotion, fear, mental) *Banner's Call* The conquering army manifests before you and your allies, letting out a battle cry of victory and devotion. Each enemy within an 80-foot emanation must attempt a Will save.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Frightened]] 2.
- **Failure** The creature takes 6d12 mental damage and is [[Frightened]] 3.
- **Critical Failure** The creature takes @Damage[12d12[mental]|options:area-damage|traits:auditory,emotion,fear,mental] damage, is [[Frightened]] 4, and is [[Fleeing]] for 1 round.

**Depart** (emotion, healing, mental) *Trumpets of War* As the conquering soldiers begin to fade, their military musicians play one more triumphant song in your honor. You and all allies within 100 feet of the soldiers immediately reduce the value of any [[Clumsy]], [[Drained]], [[Enfeebled]], [[Frightened]], [[Sickened]], and [[Stupefied]] conditions by 2 and gain a +2 status bonus to all attacks, saving throws, skill checks, and DCs for 3 rounds.

> [!danger] Effect: Spell Effect: Conquering Soldiers (Depart)

**Source:** `= this.source` (`= this.source-type`)
