---
type: creature
group: ["Fey", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Marrmora"
level: "15"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fey"
trait_02: "Fire"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+27; [[Low-Light Vision]]"
languages: "Common, Elven, Fey"
skills:
  - name: Skills
    desc: "Acrobatics +25, Athletics +25, Deception +30, Intimidation +30, Nature +30, Stealth +27, Survival +27"
abilityMods: ["+6", "+4", "+8", "+4", "+6", "+8"]
abilities_top: []
armorclass:
  - name: AC
    desc: "37; **Fort** +29, **Ref** +25, **Will** +27"
health:
  - name: HP
    desc: "280; **Immunities** fire; **Weaknesses** cold iron 15; **Resistances** physical 10 except slashing"
abilities_mid:
  - name: "Absorb Flame"
    desc: "`pf2:r` **Trigger** The marrmora is targeted by a fire spell or effect, or is in the area of a fire effect <br>  <br> **Effect** The marrmora is healed by the fire damage, regaining Hit Points equal to half the damage the fire effect would have dealt."
  - name: "Fascination of Flame"
    desc: "30 feet. A creature that enters or begins its turn in this aura's emanation must attempt a DC 33 [[Will]] save. Regardless of the result of the saving throw, the creature is temporarily immune for 1 minute. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature loses any resistance to fire for 1 round. <br> - **Failure** The creature loses any resistance to fire for 1 hour. <br> - **Critical Failure** The creature loses any resistance to fire for 1 hour and gains weakness 15 to fire for the same duration."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +29 (`pf2:1`) (unarmed), **Damage** 3d6+14 slashing plus 3d6 fire plus 1d6 fire"
  - name: "Ranged strike"
    desc: "Flame Jet +29 (`pf2:1`) (fire, range 40 ft.), **Damage** 6d6 fire plus 2d6 fire"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 36, attack +28<br>**7th** [[Volcanic Eruption]]<br>**5th** [[Elemental Form (fire elemental only)]]<br>**4th** [[Fire Shield]], [[Wall of Fire]]<br>**3rd** [[Fireball]], [[Fireball]]<br>**2nd** [[Blazing Bolt]], [[One with Plants (at will; appears as a burnt, dead tree)]]<br>**1st** [[Ignition]]"
abilities_bot:
  - name: "Igniting Assault"
    desc: "`pf2:1` **Requirements** The marrmora is not under the effect of [[Fire Shield]] <br>  <br> **Effect** The marrmora makes a claw Strike. If it hits, it can immediately cast one of its available fire shield innate spells as a free action."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

On the First World, marrmoras dwell in ruined wildlands perpetually scourged by fire and rarely, if ever, travel elsewhere. When a wildfire devastates a wilderness region on the Universe and results in the death of other fey, marrmoras can be drawn across the planar boundary to revel in the resulting destruction. They seek to reignite the fires that beckoned them, to gather up and feed upon the charred remains of those who perished within (particularly the bodies of dead fey), though they do grow homesick if they spend too much time away from the First World. They're burdened by a capricious but persistent rage and are unfailingly cruel. While they're capable of negotiation and intelligent interaction, they almost never bargain in good faith and typically interact with others only as a means to more efficiently spread their fiery devastation.

A marmorra's twisted appearance evokes the look of an arboreal whose bark has been burnt down to charcoal. They have nearly featureless faces and hands ending in long, sharp claws. Their broken flesh looks like charcoal-burnt wood, riddled with cracks that still glow with an unwholesome heat. They trail ash wherever they walk, and wisps of smoke curl off of their bodies. Though marrmoras enjoy the sight of any woodland and its inhabitants roasting in their carefully curated fires, there's little that brings more pleasure to the monstrous fey than the sight of intelligent plant creatures cooking to a crisp.

```statblock
creature: "Marrmora"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
