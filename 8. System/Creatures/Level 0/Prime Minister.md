---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Prime Minister"
level: "0"
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
    desc: "+9"
languages: "Common (up to 3 additional languages spoken in their nation)"
skills:
  - name: Skills
    desc: "Deception +22, Diplomacy +22, Intimidation +19, Society +22, Guild Lore +17, Legal Lore +19"
abilityMods: ["+0", "+2", "+1", "+3", "+3", "+4"]
abilities_top:
  - name: "+10 to Sense Motive"
    desc: ""
  - name: "Political Specialist"
    desc: "For encounters involving politics, the prime minister is a 10th-level challenge."
  - name: "Unshakable Confidence"
    desc: "All attempts to [[Coerce]] the prime minister have a result one degree worse."
armorclass:
  - name: AC
    desc: "14; **Fort** +6, **Ref** +3, **Will** +19"
health:
  - name: HP
    desc: "15"
abilities_mid:
  - name: "Cutting Counterpoint"
    desc: "`pf2:r` **Trigger** The prime minister hears a creature attempt a Deception, Diplomacy, or an Intimidation check against any creature other than the prime minister <br>  <br> **Effect** The prime minister interrupts with a witty barb, cutting the credibility of the creature's argument. The prime minister attempts their own check of the same type. If the result is higher than that of the triggering check, the triggering check is considered a failure regardless of its roll. <br>  <br> In extended negotiations, like a Victory Point challenge, the prime minister can't use this ability again until every creature in the discussion has had an opportunity to attempt a check (even if they decide not to make one)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Rapier +5 (`pf2:1`) (deadly d8, disarm, finesse), **Damage** 1d6 piercing"
  - name: "Melee strike"
    desc: "Fist +5 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The prime minister is the leader of a nation's bureaucracy. They are experienced politicians in charge of the laws and regulations of their territory, answering only to a monarch, if there is one. Often, though, a vote of "No Confidence" or similar legal procedure exists for removing the prime minister.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Prime Minister"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
