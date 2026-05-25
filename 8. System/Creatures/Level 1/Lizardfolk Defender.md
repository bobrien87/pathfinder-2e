---
type: creature
group: ["Humanoid", "Lizardfolk"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Lizardfolk Defender"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Lizardfolk"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7"
languages: "Draconic, Iruxi, Common"
skills:
  - name: Skills
    desc: "Acrobatics +5, Athletics +6, Stealth +5"
abilityMods: ["+3", "+2", "+3", "-1", "+2", "+0"]
abilities_top:
  - name: "Deep Breath"
    desc: "A lizardfolk defender can hold their breath for 15 minutes."
  - name: "Terrain Advantage"
    desc: "Non-lizardfolk creatures that are in difficult terrain or are in water and lack a swim Speed are [[Off Guard]] to the lizardfolk defender."
armorclass:
  - name: AC
    desc: "16 (18 with shield raised); **Fort** +8, **Ref** +7, **Will** +5"
health:
  - name: HP
    desc: "21"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Shield Block"
    desc: "`pf2:r` **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Flail +8 (`pf2:1`) (disarm, sweep, trip), **Damage** 1d6+3 bludgeoning"
  - name: "Melee strike"
    desc: "Jaws +8 (`pf2:1`) (unarmed), **Damage** 1d6+3 piercing"
  - name: "Melee strike"
    desc: "Tail +8 (`pf2:1`) (agile), **Damage** 1d4+3 bludgeoning"
  - name: "Melee strike"
    desc: "Javelin +7 (`pf2:1`) (thrown 30), **Damage** 1d6+3 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A lizardfolk defender serves as a protector of the young, guardian of the settlement, and when no other options are available, a soldier in times of war. They eagerly rise to the defense of their kin but do not revel in battle. An iruxi defender would rather turn back intruders and allow them to flee with the knowledge they were beaten, in hopes that such word prevents further invasions, but they are not naive. Iruxis understand the need for revenge, and when they allow a foe to escape, they do not forget.

Capable and adaptable predators, the reptilian beings known as lizardfolk are heirs to truly ancient civilizations. Their oral traditions cover thousands of years, and they revere the bones of their ancestors. Fossilized lizardfolk are even built into the walls of lizardfolk's stone and glass cities, to allow these predecessors to watch over their kin. Lizardfolk likewise have longstanding traditions of religious worship and astrology, with eyes on the past, the future, and the stars whenever they make a large decision. Their long history has taught them to be patient in all things, though this has seen them losing ground to hastier peoples in modern times.

Lizardfolk refer to themselves as "iruxi," though they have taken their common moniker among other peoples in stride. Most of their settlements are entirely communal, with hatchlings raised by anyone with the time and temperament for such a role. Iruxis dwell and thrive in all tropical and temperate biomes, but they are most at home in swamplands, coastal regions, and river lands. They are talented swimmers, and many of their major cities are partially submerged to take advantage of this fact, causing them to often be overlooked by others. Fish and aquatic plants make up a large part of their preferred diets.

```statblock
creature: "Lizardfolk Defender"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
