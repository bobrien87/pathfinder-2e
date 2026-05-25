---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Cult Leader"
level: "7"
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
    desc: "+14"
languages: "Common"
skills:
  - name: Skills
    desc: "Arcana +13, Deception +16, Diplomacy +14, Intimidation +16, Occultism +17, Society +13, Cult Lore (applies to the leader's own cult) +19"
abilityMods: ["+0", "+4", "+1", "+4", "+3", "+5"]
abilities_top: []
armorclass:
  - name: AC
    desc: "23; **Fort** +12, **Ref** +15, **Will** +18"
health:
  - name: HP
    desc: "95"
abilities_mid:
  - name: "Protect the Master!"
    desc: "`pf2:r` **Trigger** The cult leader is targeted with an attack, and a lower-ranking cultist is adjacent to them <br>  <br> **Effect** The cult leader orders their cultist to leap in front of the attack. The cultist and cult leader swap places, and the cultist becomes the target of the attack. If the cultist has Fanatical Frenzy or a similar ability, they can activate it as a reaction if they take damage from the triggering attack."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +16 (`pf2:1`) (agile, finesse, magical, versatile s), **Damage** 1d6+6 piercing plus 2d8 void"
  - name: "Melee strike"
    desc: "Fist +15 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+6 bludgeoning"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 26, attack +18<br>**4th** (3 slots) [[Honeyed Words]], [[Outcast's Curse]], [[Suggestion]]<br>**3rd** (4 slots) [[Enthrall]], [[Haste]], [[Mind Reading]]<br>**2nd** (4 slots) [[Augury]], [[Calm]], [[Laughing Fit]], [[Stupefy]]<br>**1st** (4 slots) [[Bless]], [[Daze]], [[Detect Magic]], [[Grim Tendrils]], [[Guidance]], [[Illusory Disguise]], [[Lock]], [[Phantasmal Minion]], [[Shield]], [[Void Warp]]"
abilities_bot:
  - name: "Gather Converts"
    desc: "`pf2:3` With a short emotional phrase, the cult leader tries to sway the public to do their bidding. The cult leader tries to convince up to four bystanders in a crowd to cause a commotion, turn against a person or group, leave the area, protect the cult leader, or calm down. The cult leader attempts a single [[Deception]] check against the highest Perception DC among the targets. <br> - **Critical Success** The targets believe the lie and act as directed for 1 minute. Additionally, one bystander remains by the cult leader's side, influenced enough to join the cult. All other targets become wise to the cult leader after 1 minute, at which point their attitude toward the leader worsens by one step. <br> - **Success** As a critical success, but no bystander joins the cult permanently. <br> - **Critical Failure** The crowd is unmoved and unamused, and their attitude toward the cult leader worsens by one step."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A career of mystical accomplishments combined with a lifetime of subterfuge and intimidation has elevated this occultist to a powerful position.

Hidden secrets and occult powers have an irresistible lure for many. Since the majority of these NPCs are spellcasters, consider using alternative spell lists to adjust their themes.

```statblock
creature: "Cult Leader"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
