---
type: creature
group: ["Construct", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Charnel Creation"
level: "8"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +19"
abilityMods: ["+5", "-1", "+3", "-5", "+0", "-5"]
abilities_top: []
armorclass:
  - name: AC
    desc: "26; **Fort** +18, **Ref** +14, **Will** +15"
health:
  - name: HP
    desc: "140; **Immunities** electricity; **Resistances** physical 5 except adamantine, spells 5 except fire"
abilities_mid:
  - name: "Berserk"
    desc: "A severely damaged charnel creation has a chance of going berserk. If it has 40 or fewer HP at the start of its turn, the creation must succeed at a DC 5 flat check or go berserk. A berserk creation wildly attacks the nearest living creature, or the nearest object if no creatures are nearby. A creation loses its immunity to mental effects while berserk."
  - name: "Electric Healing"
    desc: "Any time a charnel creation would be affected by an effect with the electricity trait, it loses any [[Slowed]] condition it has and gains HP equal to half the damage the spell would have dealt. If the creation starts its turn in an area that deals electricity damage, it gains 2d4 HP."
  - name: "Electric Reflexes"
    desc: "`pf2:r` **Trigger** The creation would be affected by an effect with the electricity trait and a creature is in its reach <br>  <br> **Effect** The creation lashes out and tries to grab a nearby creature. The creation attempts an Athletics check to [[Grapple]] a creature within reach. The creature also takes 3d6 electricity damage on a success, or 6d6 electricity damage on a critical success."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +20 (`pf2:1`) (magical, reach 10 ft., unarmed), **Damage** 2d10+7 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Berserk Slam"
    desc: "`pf2:1` **Requirements** The charnel creation is berserk <br>  <br> **Effect** The charnel creation Strikes with its fist at a –1 circumstance penalty. If it hits, it deals 1d6 extra damage and knocks the target [[Prone]]."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Made of odd scraps of skin and muscle, a charnel creation is a grotesque parody of life. Though it has no mind, it can still go into a berserk rage when harmed, giving it a faint semblance of emotion. These constructs are often fashioned to guard the secret laboratories, unhallowed funerary grounds, and bloody charnel houses of fleshwarpers and necromancers who feel no compunctions about desecrating corpses for their own ends. Though the first charnel creation is believed to have been a misguided attempt to create life from simple base elements, these monstrosities are far from human. In isolated cases, echoes of a personality might rise in a charnel creation if the brain used as part of its construction belonged to a particularly powerful personality, but such tragic instances are (thankfully) rare in the extreme.

```statblock
creature: "Charnel Creation"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
