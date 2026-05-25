---
type: creature
group: ["Daemon", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Thanadaemon"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Daemon"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+26; [[Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Common, Daemonic (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Arcana +22, Deception +26, Intimidation +26, Religion +22, Styx Lore +24"
abilityMods: ["+6", "+6", "+4", "+3", "+5", "+7"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Draining Strike"
    desc: "When a thanadaemon damages a living creature with a melee Strike, the creature must succeed at a DC 33 [[Fortitude]] save or become [[Drained]] 1. Further damage dealt by the thanadaemon increases the drained condition value by 1 on a failed save, to a maximum of [[Drained]] 4."
armorclass:
  - name: AC
    desc: "34; **Fort** +21, **Ref** +23, **Will** +26"
health:
  - name: HP
    desc: "270; **Immunities** death effects; **Weaknesses** holy 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Terrifying Gaze"
    desc: "30 feet. When a creature ends its turn in the aura, it must attempt a DC 30 [[Will]] save. If the creature fails, it becomes [[Frightened]] 2. The creature is then temporarily immune to terrifying gaze (but not Focus Gaze) for 24 hours."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bo Staff +28 (`pf2:1`) (magical, parry, reach 10 ft., trip, unholy), **Damage** 2d8+16 bludgeoning plus 1d6 void plus [[Draining Strike]]"
  - name: "Melee strike"
    desc: "Claw +27 (`pf2:1`) (agile, finesse, magical, unarmed, unholy), **Damage** 3d6+17 slashing plus [[Draining Strike]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 34, attack +24<br>**7th** [[Execute]], [[Interplanar Teleport (at will; self plus skiff and passengers only; Astral, Ethereal, and unholy planes only)]]<br>**6th** [[Teleport]], [[Truesight]] (Constant), [[Vampiric Exsanguination]]<br>**4th** [[Translocate]], [[Translocate]] (At Will)<br>**3rd** [[Slow]]"
abilities_bot:
  - name: "Focus Gaze"
    desc: "`pf2:1` The thanadaemon glares at a single creature they can see within 30 feet. If the target wasn't already [[Frightened]], they must immediately attempt a DC 33 [[Will]] save against the thanadaemon's terrifying gaze. If the target was already frightened, they must attempt a DC 33 [[Will]] save or become [[Fleeing]] for 1d4 rounds; this second effect has the incapacitation trait. After attempting its save, the creature is temporarily immune to this ability until the start of the thanadaemon's next turn."
  - name: "Soul Crush"
    desc: "`pf2:2` **Requirements** The thanadaemon has a soul gem <br>  <br> **Effect** The thanadaemon crushes the soul gem in one hand and gains fast healing 15 for 1 minute. <br>  <br> > [!danger] Effect: Soul Crush (Healing)"
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Also known as the deacons of death, thanadaemons represent death via old age. They are among the most patient daemons, and prefer to bide their time to enact far-reaching, decades-long plans rather than fight (though they are still deadly foes). Like the Horseman of Death, they ply the waters of the River Styx in search of wayward souls. Rarely are thanadaemons seen without a trademark oar (which they wield as a bo staff), a tool they use to navigate the river's muck-ridden channels and turbulent rapids.

Daemons form from the most despicable souls and personify forms of death.

```statblock
creature: "Thanadaemon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
