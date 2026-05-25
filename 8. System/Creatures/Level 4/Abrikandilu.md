---
type: creature
group: ["Demon", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Abrikandilu"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]]"
languages: "Chthonian, Draconic, Empyrean (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Athletics +12, Intimidation +8"
abilityMods: ["+4", "+1", "+3", "-2", "+2", "+0"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Loathsome Bite"
    desc: "When an abrikandilu hits a creature with their jaws Strike, the creature becomes infected with the demon's self-loathing. The creature must succeed at a DC 21 [[Will]] save to avoid gaining a –1 status penalty to Charisma-based checks. This penalty is cumulative up to –3, and remains even if the wounds are healed. The penalty is reduced by 1 every 24 hours until it reaches 0. <br>  <br> > [!danger] Effect: Loathsome Bite"
armorclass:
  - name: AC
    desc: "19; **Fort** +15, **Ref** +9, **Will** +7"
health:
  - name: HP
    desc: "70; **Weaknesses** cold iron 5, holy 5"
abilities_mid:
  - name: "Hatred of Mirrors"
    desc: "An abrikandilu loathes the sight of their reflection. When a creature Interacts with a mirror within sight of the wrecker demon, the demon takes a -2 penalty to Will saves against Intimidation checks. <br>  <br> An abrikandilu that ends their turn adjacent to a mirror or that's attacked by a creature holding a mirror takes 1d6 mental damage (this usually leads abrikandilus to focus their efforts on destroying nearby mirrors using Wreck)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +14 (`pf2:1`) (agile, unarmed, unholy), **Damage** 2d6+4 slashing"
  - name: "Melee strike"
    desc: "Jaws +14 (`pf2:1`) (unarmed, unholy), **Damage** 3d6+4 piercing plus [[Mutilating Bite]]"
  - name: "Ranged strike"
    desc: "Hurled Debris +11 (`pf2:1`) (unholy, range 20 ft.), **Damage** 2d6+4 bludgeoning"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 20, attack +12<br>**1st** [[Fear]]"
abilities_bot:
  - name: "Wreck"
    desc: "`pf2:1` The abrikandilu makes two claw Strikes against an unattended object or held mirror. Held mirrors use the holding character's AC. <br>  <br> If both Strikes hit, combine their damage for the purpose of overcoming any Hardness or resistance. <br>  <br> These Strikes don't count toward the abrikandilu's multiple attack penalty, nor does that penalty apply to these Strikes."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Wrecker demons, also known as abrikandilus, despise beautiful things and do everything in their power to destroy both people and objects regarded as such. An abrikandilu forms from the souls mortals who were vandals, misanthropes, or defacers of artwork, particularly if their destructive actions stemmed from feelings of powerful envy.

An abrikandilu loathes only one thing more than beauty: their own visage. The mere sight of their face-reflected in a mirror, a shield, or even a pool of water- can send a wrecker demon into a rage. Many demon slayers leverage tactic to their advantage, venturing into battle with polished steel shields and cold iron blades at the ready.

Mortal souls that have been twisted and corrupted by sin sometimes arise in the afterlife as demons. These powerful and destructive fiends seek to spread their particular sin to warp more souls, thereby bolstering their numbers and continuing the cycle.

```statblock
creature: "Abrikandilu"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
