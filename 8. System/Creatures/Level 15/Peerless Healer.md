---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Peerless Healer"
level: "15"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+25"
languages: "Common, Empyrean"
skills:
  - name: Skills
    desc: "Diplomacy +26, Medicine +33, Nature +27, Religion +25, Society +23"
abilityMods: ["+3", "+1", "+3", "+2", "+4", "+5"]
abilities_top:
  - name: "Doctor's Hand"
    desc: "When the peerless healer rolls a critical failure on a check to [[Treat Disease]], [[Treat Poison]], or [[Treat Wounds]], they get a failure instead."
  - name: "Medical Specialist"
    desc: "The peerless healer is a 17th-level challenge for contests of medicine."
  - name: "Community Healer"
    desc: "When [[Treating Disease]] or [[Treating Wounds]], the humanitarian healer can treat up to eight targets. In addition, each time the peerless healer successfully Treats Wounds, they can also either reduce the value of one [[Clumsy]], [[Enfeebled]], [[Drained]], or [[Stupefied]] condition affecting a single patient by 2 or cast a 7th-rank [[Clear Mind]], [[Sound Body]], or [[Sure Footing]] spell on one patient without expending a spell slot."
  - name: "Healing Hands"
    desc: "When the peerless healer casts [[Heal]], they roll d10s instead of d8s."
armorclass:
  - name: AC
    desc: "35; **Fort** +26, **Ref** +24, **Will** +27"
health:
  - name: HP
    desc: "200; **Resistances** poison 15"
abilities_mid:
  - name: "Healing Echo"
    desc: "`pf2:0` **Trigger** The peerless healer restores Hit Points to an ally using [[Heal]] <br>  <br> **Effect** One willing creature within 30 feet who didn't benefit from the triggering spell regains Hit Points equal to half the healing granted. The peerless healer can't use Healing Echo again for 1d4 rounds."
  - name: "+2 Status vs. Poison and Disease"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +24 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+9 bludgeoning plus 4d8 vitality"
  - name: "Melee strike"
    desc: "Staff +25 (`pf2:1`) (magical, two hand d8), **Damage** 2d4+9 bludgeoning plus 4d8 vitality"
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 37, attack +29<br>**8th** (3 slots) [[Moment of Renewal]]<br>**7th** (4 slots) [[Regenerate]]<br>**6th** (4 slots) [[Field of Life]]<br>**5th** (4 slots) [[Breath of Life]], [[Sending]], [[Truespeech]]<br>**4th** (4 slots) [[Creation]], [[Fly]], [[Talking Corpse]], [[Unfettered Movement]], [[Vital Beacon]]<br>**3rd** (4 slots) [[Heroism]], [[Locate]], [[Locate]], [[Ring of Truth]], [[Safe Passage]]<br>**2nd** (4 slots) [[Cleanse Affliction]], [[Clear Mind]], [[Everlight]], [[Resist Energy]], [[Revealing Light]], [[Share Life]], [[Sound Body]], [[Sure Footing]], [[Water Breathing]]<br>**1st** (4 slots) [[Air Bubble]], [[Cleanse Cuisine]], [[Create Water]], [[Detect Magic]], [[Divine Lance]], [[Heal]], [[Heal]], [[Message]], [[Sanctuary]], [[Shield]], [[Stabilize]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Peerless healers are legendary, blending divine and natural medicine. Often pillars in their respective communities, they see to the health of the populace.

The world is a dangerous place. Thankfully, there are those who devote their lives to easing the pain and suffering of others.

```statblock
creature: "Peerless Healer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
