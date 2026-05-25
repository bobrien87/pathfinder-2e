---
type: creature
group: ["Humanoid", "Orc"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Orc Veteran"
level: "1"
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
    desc: "+6; [[Darkvision]]"
languages: "Orcish, Common"
skills:
  - name: Skills
    desc: "Athletics +7, Intimidation +4, Survival +4"
abilityMods: ["+4", "+2", "+3", "-1", "+1", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +8, **Ref** +7, **Will** +4"
health:
  - name: HP
    desc: "23"
abilities_mid:
  - name: "Ferocity"
    desc: "`pf2:r` **Trigger** The monster is reduced to 0 HP. <br>  <br> **Effect** The monster avoids being knocked out and remains at 1 HP, but its [[Wounded]] value increases by 1. When it is Wounded 3, it can no longer use this ability"
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Orc Necksplitter +7 (`pf2:1`) (forceful, sweep), **Damage** 1d8+4 slashing"
  - name: "Melee strike"
    desc: "Shortsword +7 (`pf2:1`) (agile, versatile p), **Damage** 1d6+4 slashing"
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
  - name: "Melee strike"
    desc: "Javelin +5 (`pf2:1`) (thrown 30), **Damage** 1d6+4 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Orc veterans have survived several bloody and chaotic conflicts, coming out the other side with scars and experience that make them even more dangerous opponents.

Many orcs are forged in the fires of violence and conflict, often from the moment they're born. As they live lives that are frequently cut brutally short, orcs revel in testing their strength against worthy foes, whether by challenging a higher-ranking member of their community for dominance, taming a powerful beast, or slaying a fearsome monster.

Tall and powerful, with long arms and thickly muscled legs, many orcs top 7 feet in height. Their heavy limbs and broad, almost bow-legged stances combine with a tendency to slouch forward to create an almost contradictory set of circumstances where an orc can tower over other humanoids while simultaneously staring them in the eye. These features, alongside a tendency to scar easily, can make them seem quite intimidating.

The half-orc dromaars, most commonly born of unions between orcs and humans, are often tested even more harshly than their full orc kin, but those who endure these tests can rise to positions of authority. "An orc can have what an orc can hold" is a saying that not only applies to an individual's ability to secure their own destiny and position, but is also likely the root of orcs referring to their communities as holds.

```statblock
creature: "Orc Veteran"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
