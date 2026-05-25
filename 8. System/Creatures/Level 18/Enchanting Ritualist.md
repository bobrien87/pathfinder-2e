---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Enchanting Ritualist"
level: "18"
rare_01: "Uncommon"
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
    desc: "+31"
languages: "Common, Diabolic, Empyrean, Fey"
skills:
  - name: Skills
    desc: "Arcana +34, Deception +35, Diplomacy +31, Nature +34, Occultism +36, Religion +34"
abilityMods: ["+4", "+3", "+1", "+6", "+6", "+8"]
abilities_top:
  - name: "+2 Circumstance to Skill Checks for Rituals"
    desc: ""
  - name: "Fool's Feast"
    desc: "Recipients of the ritualist's generosity pay dearly if the ritualist decides to turn against them. The ritualist gets a +4 circumstance bonus to attack rolls against any creature that has willingly participated in or benefited from one of their spells or rituals conducted in the last 12 hours. A creature that didn't help conduct a ritual still qualifies if it benefited in other ways, such as drinking a serving of [[Fortifying Brew]]. <br>  <br> When the enchanting ritualist damages such a creature with a Strike, the target is affected by a 9th-rank [[Cursed Metamorphosis]] spell (DC 42). If the Strike was a critical hit, the creature gets a degree of success one worse than it rolled. Once a creature succeeds at a save against this spell, it is temporarily immune for 24 hours."
armorclass:
  - name: AC
    desc: "40; **Fort** +27, **Ref** +28, **Will** +33"
health:
  - name: HP
    desc: "320; **Resistances** mental 20"
abilities_mid:
  - name: "Aura of Contentment"
    desc: "30 feet. A creature that enters or starts its turn in the aura must succeed at a DC 38 [[Will]] save or lose the desire to do anything except rest and relax. Hostile actions taken against creatures affected by the aura end the effect. If a creature in the aura succeeds on their Will save or is the subject of a hostile action, it's temporarily immune to the aura of contentment for 24 hours. The enchanting ritualist can exempt creatures from the aura's effects."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Club +30 (`pf2:1`) (magical), **Damage** 3d6+12 bludgeoning plus 2d6 mental plus [[Fools Feast]]"
  - name: "Melee strike"
    desc: "Club +28 (`pf2:1`) (magical, thrown 10), **Damage** 3d6+12 bludgeoning plus 2d6 mental plus [[Fools Feast]]"
  - name: "Melee strike"
    desc: "Fist +28 (`pf2:1`) (agile, magical, nonlethal, unarmed), **Damage** 1d4+12 bludgeoning plus 2d6 mental plus [[Fools Feast]]"
  - name: "Ranged strike"
    desc: "Enchanting Wisps +30 (`pf2:1`) (magical, mental), **Damage** 9d6 mental plus [[Fools Feast]]"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 42, attack +34<br>**9th** (4 slots) [[Foresight]], [[Overwhelming Presence]], [[Telepathic Demand]]<br>**8th** (4 slots) [[Canticle of Everlasting Grief]], [[Quandary]], [[Spirit Song]], [[Uncontrollable Dance]]<br>**7th** (4 slots) [[Mask of Terror]], [[Project Image]]<br>**6th** (4 slots) [[Mislead]], [[Repulsion]], [[Truesight]], [[Zealous Conviction]]<br>**5th** (4 slots) [[Dreaming Potential]], [[Hallucination]], [[Scouting Eye]], [[Sending]], [[Synesthesia]], [[Truespeech]], [[Wave of Despair]]<br>**4th** (4 slots) [[Confusion]], [[Fly]], [[Honeyed Words]], [[Translocate]]<br>**3rd** (4 slots) [[Dream Message]], [[Hypnotize]], [[Levitate]]<br>**2nd** (4 slots) [[Augury]], [[Darkvision]], [[See the Unseen]], [[Status]]<br>**1st** (4 slots) [[Alarm]], [[Daze]], [[Detect Magic]], [[Fear]], [[Ill Omen]], [[Illusory Disguise]], [[Illusory Object]], [[Light]], [[Read Aura]], [[Telekinetic Hand]]"
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Possessing great stores of knowledge on mental magic and rituals, enchanting ritualists can also be solitary and capricious, tricking and transforming their visitors. The GM can change the selection of rituals this NPC knows freely, choosing any rituals of 9th rank or lower.

Hidden secrets and occult powers have an irresistible lure for many. Since the majority of these NPCs are spellcasters, consider using alternative spell lists to adjust their themes.

```statblock
creature: "Enchanting Ritualist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
