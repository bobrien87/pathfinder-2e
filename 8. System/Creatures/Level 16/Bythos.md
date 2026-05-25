---
type: creature
group: ["Aeon", "Monitor"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Bythos"
level: "16"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Aeon"
trait_02: "Monitor"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+30; [[Darkvision]]"
languages: "envisioning"
skills:
  - name: Skills
    desc: "Arcana +29, Athletics +32, Deception +25, Intimidation +25, Nature +30, Occultism +29, Religion +30, Stealth +26"
abilityMods: ["+8", "+4", "+5", "+7", "+8", "+5"]
abilities_top:
  - name: "Envisioning"
    desc: "When a bythos conveys information, it does so wordlessly through psychic projections. This acts as [[Telepathy]] with a range of 100 feet but is understandable to all creatures regardless of whether they have a language. <br>  <br> The meaning to non-aeons can be vague and is often mysterious. A bythos can use this ability to communicate flawlessly with any other aeon on the same plane."
armorclass:
  - name: AC
    desc: "39; **Fort** +25, **Ref** +26, **Will** +30"
health:
  - name: HP
    desc: "245; regeneration 15 (deactivated by spirit); **Weaknesses** spirit 15"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Regeneration 15 (Deactivated by Spirit)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Confusing Gaze"
    desc: "30 feet. A creature that ends its turn in the aura must attempt a DC 34 [[Will]] save. If it fails, it's [[Confused]] for 1 round (or 1d4 rounds on a critical failure)."
  - name: "Temporal Reversion"
    desc: "`pf2:0` **Trigger** The bythos fails or critically fails a check <br>  <br> **Frequency** once per day <br>  <br> **Effect** The bythos rerolls the triggering check and takes the better result."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +32 (`pf2:1`) (magical, reach 10 ft., unarmed), **Damage** 3d8+16 bludgeoning plus 2d8 cold"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 37, attack +27<br>**7th** [[Interplanar Teleport]], [[Planar Seal]]<br>**6th** [[Teleport]]<br>**4th** [[Planar Tether]], [[Planar Tether]] (At Will)<br>**3rd** [[Haste]], [[Slow]]<br>**2nd** [[Augury]] (At Will)"
abilities_bot:
  - name: "Aging Strikes"
    desc: "`pf2:2` The bythos make two fist Strikes against a single target. If both Strikes hit, the target attempts a DC 37 [[Fortitude]] save. Creatures that don't get weaker with age or don't age are immune (GM's discretion). <br>  <br> If a creature becomes clumsy 4, drained 4, and enfeebled 4 due to Aging Strikes, it dies of old age. <br> - **Success** The creature is unaffected. <br> - **Failure** The creature becomes [[Clumsy]] 1, [[Drained]] 1, and [[Enfeebled]] 1, or increases each of these conditions by 1. This effect is cumulative with other aging strikes from bythoses, to a maximum of clumsy 4, drained 4, and enfeebled 4. <br> - **Critical Failure** As failure, but the creature becomes [[Clumsy]] 2, [[Drained]] 2, and [[Enfeebled]] 2, or increases these conditions by 2."
  - name: "Focused Gaze"
    desc: "`pf2:1` The bythos focuses its gaze on a creature it can see within 30 feet. The target must attempt a save against the bythos's confusing gaze. A bythos can't use this ability against the same creature more than once per turn."
  - name: "Temporal Flurry"
    desc: "`pf2:2` The bythos makes four fist Strikes. Its multiple attack penalty increases normally with each attack."
  - name: "Temporal Strike"
    desc: "`pf2:2` The bythos touches a creature or object to displace it from time. The target attempts a DC 37 [[Fortitude]] save. <br> - **Critical Success** The target is unaffected. <br> - **Success** Time flows around the target; the target is [[Slowed]] 1 for 1 round. <br> - **Failure** The target disappears from the present moment and reappears in the same location 1d4 rounds later as if no time had passed for it. If a creature or object occupies that space when the target returns, the target appears in the closest available space to its original location. <br> - **Critical Failure** As failure, but the target is [[Slowed]] 1 for an extra 1d4 rounds after it returns."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The bythos is a guardian of space and time and ever seeks those who misuse planar and temporal magic. A bythos is a roughly humanoid creature with four arms and a body made of swirling clouds and mist. Despite their appearance, their body feels like dry stone. A bythos seeks out paradoxes caused by irresponsible planar or dimensional travelers and repairs breaches where the barriers between planes have become thin or damaged. If the mortals responsible remain in the area and cannot be convinced to cease their activities, the bythos has no qualms about removing them. Using their ability to manipulate time, a bythos might cause an opponent to quickly die of old age as time speeds up around them or cause a target to disappear from time and space.

```statblock
creature: "Bythos"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
