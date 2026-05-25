---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sylph Sneak"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Sylph"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5"
languages: "Common, Sussuran"
skills:
  - name: Skills
    desc: "Acrobatics +7, Deception +6, Diplomacy +6, Society +4, Stealth +7, Thievery +7"
abilityMods: ["+0", "+4", "+1", "+1", "+0", "+3"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The sylph sneak's Strikes deal 1d6 extra precision damage to [[Off Guard]] creatures."
  - name: "Surprise Attacker"
    desc: "On the first round of combat, creatures that haven't acted yet are [[Off Guard]] to the sylph sneak."
  - name: "Wind's Guidance"
    desc: "When the sylph sneak attacks with a thrown weapon, the range increment increases by 10 feet."
armorclass:
  - name: AC
    desc: "18; **Fort** +4, **Ref** +9, **Will** +8"
health:
  - name: HP
    desc: "17"
abilities_mid:
  - name: "Deflecting Gale"
    desc: "`pf2:r` **Trigger** The sylph sneak is the target of a physical ranged attack <br>  <br> **Requirements** The sylph sneak is aware of the attack <br>  <br> **Effect** A swift gale whips up between the sylph sneak and the source of the ranged attack, giving the sneak a +3 status bonus to AC against the triggering attack. If the attack misses, the wind deflected it. The wind can't deflect unusually large or heavy ranged projectiles (such as boulders or ballista bolts)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Starknife +9 (`pf2:1`) (agile, deadly d6, finesse, versatile s), **Damage** 1d4+2 piercing"
  - name: "Melee strike"
    desc: "Starknife +9 (`pf2:1`) (agile, deadly d6, thrown 30, versatile s), **Damage** 1d4+2 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Born with elemental gales coursing through their breath, sylphs are wispy planar scions whose bodies seem caught in a perpetual, gentle breeze. Most commonly born of unions between mortals and jaathoom, sylphs are quick-witted and creative, but they're prone to flights of fancy and tend to be easily distracted.

Sylphs are notorious for their practice of "listening to the wind," which most others dismiss as a fancy name for eavesdropping. Yet this custom means much more to sylphs, who spend hours listening to the stories brought to them on the proverbial breeze. While some less scrupulous sylphs can use the information they learn to blackmail or abuse others, most of them see listening to the wind as their way of staying connected to the world around them while still keeping it comfortably at arm's length. Certainly, the typical sylph sneak doesn't seek to use what they learn for ill but instead warns others of dangers yet unrealized or prepares themself for a dangerous task.

```statblock
creature: "Sylph Sneak"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
