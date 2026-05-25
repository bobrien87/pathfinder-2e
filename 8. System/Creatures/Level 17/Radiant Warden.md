---
type: creature
group: ["Construct"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Radiant Warden"
level: "17"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Construct"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+30; [[Darkvision]]"
languages: "any one ancient language (such as Jistkan)"
skills:
  - name: Skills
    desc: "Arcana +32, Athletics +33, Occultism +32, Astronomy Lore +36"
abilityMods: ["+9", "+6", "+5", "+6", "+5", "+0"]
abilities_top:
  - name: "Radiant Blow"
    desc: "When a creature is hit by the radiant warden's hammer Strike, a flash of radiant energy attempts to anchor the creature in place. The creature must attempt a DC 38 [[Will]] save; on a failure, the creature can't use any teleportation effects for 1 minute. On a critical failure, the creature is also permanently [[Blinded]]."
armorclass:
  - name: AC
    desc: "40; **Fort** +32, **Ref** +29, **Will** +28"
health:
  - name: HP
    desc: "300; **Resistances** mental 15, physical 15 except adamantine"
abilities_mid:
  - name: "Gatekeeper Aura"
    desc: "60 feet. A creature that uses a teleportation ability within the aura's emanation or enters it via a teleportation ability must succeed a DC 38 [[Will]] save or become [[Sickened]] 1 and have its destination changed to a point of the radiant warden's choosing within the aura. On a successful save, the creature arrives as intended but is still sickened 1."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Hammer +32 (`pf2:1`) (magical, reach 15 ft., shove), **Damage** 3d12+15 bludgeoning plus [[Radiant Blow]]"
  - name: "Ranged strike"
    desc: "Radiant Beam +31 (`pf2:1`) (force, magical, range 30 ft.), **Damage** 4d10+6 force"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 38, attack +30<br>**8th** [[Pinpoint]]<br>**7th** [[Planar Seal]]<br>**6th** [[Collective Transposition]], [[Teleport]], [[Wall of Force]]<br>**4th** [[Translocate]] (At Will)"
abilities_bot:
  - name: "Orrery"
    desc: "`pf2:1` Until it acts, the radiant warden appears to be an orrery (or similar large mechanical contraption, such as a telescope). It has an automatic result of 53 on Deception checks and DCs to convincingly pass as such a machine."
  - name: "Radiant Blast"
    desc: "`pf2:2` The radiant warden releases a @Template[type:cone|distance:50] of bright energy that deals @Damage[10d12[force]|options:area-damage] damage (DC 38 [[Reflex]] save). The radiant warden can't use Radiant Blast for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The enigmatic and strange radiant wardens were constructed thousands of years ago to protect observatories and scholars against the incursion of alien aggressors from the Dominion of the Black. Over time, their roles as guardians expanded to include watching over any region where the laws of time and space have worn thin, particularly near portals and permanent gates between planets, planes, or dimensions.

Named for both the radial nature of the concentric rings that make up their bodies as well as the glowing radiance of their attacks, radiant wardens carry on their orders, defending sites from invasion with single-minded purpose.

```statblock
creature: "Radiant Warden"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
