---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "9"
traits: ["[[Mythic]]", "[[Water]]"]
cast: "1 day"
range: "10 feet"
targets: "body of water no larger than a 7-mile radius area"
duration: "unlimited"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You invoke consciousness in a large body of water, such as a coastline, lake, or lagoon. An ancient elemental spirit awakens in the water, seeking instantly to defend itself from aggressors or punish trespassers. You must cast this ritual either directly above the surface of the water or completely submerged at the bottom of the body of water. Such spirits are known to crash ships, devastate shores, and drag enemies under the waves, but can also respond favorably to competent casters.

This new entity must be appeased by those who sail it. Appeasing the spirit requires a [[Diplomacy]] check or [[Nature]] check at the ritual's casting DC. Those negotiating with the spirit might make offerings to gain the spirit's favor, but such reprieve is short in duration and must be attempted each time a vessel passes near. The nature of these offerings is subject to the GM's discretion.
- **Critical Success** As success, except the spirit looks kindly on the caster and those who travel with them. The spirit never takes hostile action against them or any vessel they travel on and increases their swim Speed or their vessel's Speed by 10 feet while within the affected area. Additionally, the spirit's Strike gains the [[Improved Grab]] ability with an Athletics modifier of +38.
- **Success** The spirit takes up residence in the body of water, defending it aggressively or attacking organized threats on adjacent shores. The spirit manifests as either a massive tsunami (*GM Core* 90, 96) that repeats every hour or a massive fist of water that can make a melee Strike every round against any target within the affected area. This Strike has a +33 modifier and deals 3d8+19 bludgeoning damage. The spirit can make this Strike against two targets within 30 feet, rolling once to attack and comparing the result against the AC of both targets.
- **Failure** The ritual has no effect, though tides and waves are more severe than normal for 24 hours.
- **Critical Failure** The ritual backfires, causing four Elemental Tsunamis to appear surrounding the casters and attack them for their insolence. If not defeated, the tsunamis remain for 1 week, attacking any waterborne vessels within the targeted area.

**Source:** `= this.source` (`= this.source-type`)
