---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Knight"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +17, Diplomacy +12, Intimidation +16, Society +13, Warfare Lore +15"
abilityMods: ["+4", "+3", "+3", "+0", "+2", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "25 (27 with shield raised); **Fort** +14, **Ref** +14, **Will** +13"
health:
  - name: HP
    desc: "110"
abilities_mid:
  - name: "Knight's Courage"
    desc: "Any time the knight gains the [[Frightened]] condition, they reduce its value by 1."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Shield Block"
    desc: "`pf2:r` The knight can Shield Block for an adjacent ally, preventing that ally from taking damage instead of themself. <br>  <br> **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bastard Sword +18 (`pf2:1`) (magical, two hand d12), **Damage** 1d8+10 slashing"
  - name: "Melee strike"
    desc: "Spear +17 (`pf2:1`), **Damage** 1d6+10 piercing"
  - name: "Melee strike"
    desc: "Spear +17 (`pf2:1`) (thrown 20), **Damage** 1d6+10 piercing"
  - name: "Melee strike"
    desc: "Gauntlet +17 (`pf2:1`) (agile, free hand), **Damage** 1d4+10 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Intimidating Strike"
    desc: "`pf2:2` The knight makes a melee Strike. If it hits and deals damage, the target is [[Frightened]] 1, or [[Frightened]] 2 on a critical hit."
  - name: "Rearming Advance"
    desc: "`pf2:1` The knight Strides or Steps. During this movement, they can Interact to swap from wielding their bastard sword in two hands to wielding it in one hand and wielding their shield in the other, or vice versa. This Interact action doesn't trigger reactions that can be triggered by manipulate actions."
  - name: "Warding Shift"
    desc: "`pf2:1` **Requirements** The knight is adjacent to a willing ally <br>  <br> **Effect** The knight moves an adjacent willing ally 5 feet in any direction and can Step into the space the ally vacated."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Elite fighters from the lowest ranks of nobility, knights are proud champions of their court. Unlike other nobles, knights must earn their title through loyalty and strength-of-arms rather than inheritance. Ideals such as chivalry, honor, and virtue are associated with knights but not all meet such romantic standards.

The denizens of a noble court are the most powerful people in a civilization, primed with wealth, station, and authority above the common people.

```statblock
creature: "Knight"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
