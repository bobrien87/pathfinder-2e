---
type: creature
group: ["Holy", "Human"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Champion of Shelyn"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Holy"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +17, Diplomacy +16, Performance +14, Religion +15, Society +12"
abilityMods: ["+4", "+1", "+2", "+1", "+2", "+3"]
abilities_top:
  - name: "Blessed Weapon"
    desc: "If a champion's glaive Strike is a critical hit, the weapon deals an additional 1d6 persistent vitality damage, and they can force the target to move 5 feet in a direction of their choice."
armorclass:
  - name: AC
    desc: "25; **Fort** +15, **Ref** +12, **Will** +15"
health:
  - name: HP
    desc: "120"
abilities_mid:
  - name: "Champion's Aura"
    desc: "15 feet. <br>  <br> Any follower of [[Shelyn]] in the aura knows the champion is a champion of Shelyn. At the end of the champion's turn, each ally in the aura reduces its [[Frightened]] value by 1. The aura can be suppressed or resumed with a single action, which has the concentrate trait, and ends if the champion falls [[Unconscious]]."
  - name: "Champion's Courage"
    desc: "When the champion becomes [[Frightened]], they reduce the condition value by 1 (to a minimum of 0)."
  - name: "Liberating Step"
    desc: "`pf2:r` **Trigger** An enemy damages, grabs, or restrains the champion's ally, and both are in the champion's aura <br>  <br> **Effect** The champion frees an ally from restraint. If the trigger was an ally taking damage, the ally gains resistance 10 to all damage against the triggering damage. <br>  <br> > [!danger] Effect: Liberating Step <br>  <br> The ally can attempt to break free of effects grabbing, [[Restraining]], [[Immobilizing]], or [[Paralyzing]] them. They either attempt a new save against one such effect that allows a save or attempt to [[Escape]] from one effect as a free action. Whether or not it needed to escape, the ally can then Step as a free action if it's able to move."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Glaive +18 (`pf2:1`) (deadly d8, forceful, magical, reach), **Damage** 1d8+10 slashing plus 1d6 vitality"
  - name: "Melee strike"
    desc: "Fist +17 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+10 bludgeoning"
  - name: "Ranged strike"
    desc: "Crossbow +14 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8+6 piercing"
spellcasting:
  - name: "Champion Devotion Spells"
    desc: "DC 22, attack +14<br>**1st** [[Lay on Hands]], [[Protector's Sacrifice]]"
abilities_bot:
  - name: "Smite"
    desc: "`pf2:1` The champion chooses one enemy they can see. Their Strikes against that enemy gain a +4 status bonus to damage, or +8 if the target is unholy. <br>  <br> This benefit lasts until the start of the champion's next turn, but if the target takes a hostile action against the champion or one of their allies, the duration is extended until the end of the target's next turn (this can be extended indefinitely if the target keeps taking hostile actions on subsequent rounds)."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Champions are bastions of their deities' virtues and are living beacons for their causes. Those who walk these paths must adhere to the tenets of their patron deity or risk losing their abilities altogether. The champion depicted here follows the example of Shelyn, embodying the spirit of inspiring beauty and fighting for the cause of peace.

Religions inspire devout individuals to uphold their tenets.

```statblock
creature: "Champion of Shelyn"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
