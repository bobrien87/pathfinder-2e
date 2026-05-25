---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Warshard Warrior|Warshard Warrior]]"
source-type: "Remaster"
level: "12"
traits: ["[[Destiny]]", "[[Mythic]]"]
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you became infused with a shard of the god of war, you knew in your gut that your destiny would be one for the ages—yet you may not, at first, know the exact way such a destiny would play out. If you still carry the warshard that empowered you, you might carry it as a token or wear it as jewelry—if indeed it's not simply embedded into your body. Regardless, the warshard itself no longer has any intrinsic power of its own, and even if you toss the warshard aside, its gifts do not leave you, nor can another benefit from them. If you throw the warshard away or lose it, your destiny remains unaltered; you have, in effect, become the warshard itself. This power manifests through a weapon you wield.

When you make your daily preparations, choose one weapon in your possession in which you have at least expert proficiency. That weapon becomes your warshard weapon until you choose a different weapon in your possession during another of your daily preparations. You can choose a mundane nonmagical weapon, a weapon with magical runes, one made of an unusual material, or even a specific magic weapon such as a storm flash or a bloodletting kukri, but not an intelligent weapon or an artifact like the bastard sword Serithtial or one of the seven swords of sin. While you don't lose access to your warshard warrior feats if your warshard weapon is taken from you or destroyed, note that several of this destiny's feats require you to be wielding your warshard weapon. You can etch or remove runes from a warshard weapon normally. You can have only one warshard weapon at a time.

Your gain the [[Mythic Strike]] feat, but you can only use it with your warshard weapon. Whenever you make a Strike with your warshard weapon at mythic proficiency, you double the amount of additional damage you deal with the weapon specialization class feature. When you make Crafting checks to Repair your warshard weapon, your treat your proficiency rank in Crafting as legendary for determining how many Hit Points you restore to the item; in addition, if your Crafting result is a critical failure, you get a failure instead. You also gain the Call [[Warshard Weapon]] action.

Warshard Warrior (Rare)

**Source:** `= this.source` (`= this.source-type`)
