---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Bullet Dancer|Bullet Dancer]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Bullet Dancer Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a simple combination weapon or an attached bayonet or reinforced stock.

The fiery blaze of your weapon shocks your enemies. While in [[Bullet Dancer Stance]], when you successfully Strike an opponent with the melee form of a combination weapon or a bayonet or reinforced stock attached to a simple firearm, the next ranged Strike you make against that opponent doesn't trigger reactions that would trigger on a ranged attack, such as Reactive Strike. While in Bullet Dancer Stance, when you make a successful ranged Strike against an opponent within your melee reach using a firearm, the next melee attack against that opponent with that weapon or a weapon attached to it deals an additional 1 fire damage and 1 persistent fire damage per weapon damage die of the attached firearm.

The benefit on your next Strike from either use of Bullet Dancer Burn is lost if not used by the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
