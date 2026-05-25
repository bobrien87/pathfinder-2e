---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Warshard Warrior|Warshard Warrior]]"
source-type: "Remaster"
level: "16"
traits: ["[[Mythic]]"]
prerequisites: "Warshard Warrior Dedication"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a melee warshard weapon.

When you face multiple foes, you wield your warshard weapon with vigor. Spend 1 Mythic Point, then Step to a space where you threaten at least two opponents with your warshard weapon. Attempt two Strikes at mythic proficiency, each against a different target. If you hit with both Strikes, you gain an additional effect based on the type of damage you inflict with your weapon. Both attacks count toward your multiple attack penalty, but the penalty doesn't increase until after you've made both of them. If your weapon doesn't deal one of these three damage types, you can't use it to Divide and Conquer, and if you deal two different types of damage to each target, you don't gain any additional effect.

- **Bludgeoning** You knock your enemies around. Each damaged target becomes [[Off Guard]] until the start of your next turn.
- **Piercing** Your strikes punch through your enemies, leaving bloody wounds. Each damaged target takes 1d8 persistent,bleed damage.
- **Slashing** Your slashes leave particularly painful wounds. Each damaged target becomes [[Sickened]] 2.

**Source:** `= this.source` (`= this.source-type`)
