---
type: creature
group: ["Humanoid", "Orc"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Orc Commander"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Orc"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: "Common, Orcish"
skills:
  - name: Skills
    desc: "Athletics +8, Intimidation +6, Survival +5"
abilityMods: ["+4", "+2", "+1", "-1", "+1", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "19; **Fort** +7, **Ref** +6, **Will** +7"
health:
  - name: HP
    desc: "32"
abilities_mid:
  - name: "Ferocity"
    desc: "`pf2:r` **Trigger** The monster is reduced to 0 HP. <br>  <br> **Effect** The monster avoids being knocked out and remains at 1 HP, but its [[Wounded]] value increases by 1. When it is Wounded 3, it can no longer use this ability"
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greatclub +10 (`pf2:1`) (backswing, shove), **Damage** 1d10+4 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, shove, unarmed), **Damage** 1d4+4 bludgeoning"
  - name: "Melee strike"
    desc: "Javelin +8 (`pf2:1`) (thrown 30), **Damage** 1d6+4 piercing"
spellcasting: []
abilities_bot:
  - name: "Battle Cry"
    desc: "`pf2:1` Bellowing mightily, the orc commander gives themself and all orc allies within @Template[emanation|distance:60]{60 feet} a +1 status bonus to attack and damage rolls until the start of the orc commander's next turn. <br>  <br> > [!danger] Effect: Battle Cry"
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

When orcs raid, the strongest is chosen as the leader, backed up by their siblings and other immediate family. If leadership is contested, candidates vie for control with displays of physical prowess or stirring speeches.

Many orcs are forged in the fires of violence and conflict, often from the moment they're born. As they live lives that are frequently cut brutally short, orcs revel in testing their strength against worthy foes, whether by challenging a higher-ranking member of their community for dominance, taming a powerful beast, or slaying a fearsome monster.

Tall and powerful, with long arms and thickly muscled legs, many orcs top 7 feet in height. Their heavy limbs and broad, almost bow-legged stances combine with a tendency to slouch forward to create an almost contradictory set of circumstances where an orc can tower over other humanoids while simultaneously staring them in the eye. These features, alongside a tendency to scar easily, can make them seem quite intimidating.

The half-orc dromaars, most commonly born of unions between orcs and humans, are often tested even more harshly than their full orc kin, but those who endure these tests can rise to positions of authority. "An orc can have what an orc can hold" is a saying that not only applies to an individual's ability to secure their own destiny and position, but is also likely the root of orcs referring to their communities as holds.

```statblock
creature: "Orc Commander"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
