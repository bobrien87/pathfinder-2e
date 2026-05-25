---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Exiled Revolutionary"
level: "10"
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
    desc: "+17"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +18, Athletics +15, Deception +19, Diplomacy +19, Intimidation +17, Society +20, Stealth +20, Thievery +18, Lore (home region or settlement) +22"
abilityMods: ["+4", "+5", "+0", "+3", "+2", "+4"]
abilities_top:
  - name: "+3 to Sense Motive"
    desc: ""
  - name: "Former Courtier"
    desc: "An exiled revolutionary remembers well their former realm. In their home realm, be it a manor, castle, or capital city, the exiled revolutionary gains a +4 circumstance bonus to Perception checks and Will saves, and to Deception, Diplomacy, Intimidation, and Stealth checks, and is a 12th-level challenge in the arena of noble politics."
  - name: "Sneak Attack"
    desc: "The exiled revolutionary deals an additional 2d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "28; **Fort** +17, **Ref** +20, **Will** +17"
health:
  - name: HP
    desc: "140"
abilities_mid:
  - name: "Follow Me"
    desc: "20 feet. This aura is active only while in the exiled revolutionary's home realm, as they share knowledge to avoid guard patrols and get past checkpoints. Any ally in the aura gets a +2 circumstance bonus to Deception and Stealth checks."
  - name: "It's... You!"
    desc: "When the exiled revolutionary sees or hears someone who was part of their downfall in person, they break cover and attack their betrayer immediately, even if their actions would doom them and their allies. The revolutionary must succeed at a DC 35 [[Will]] save or be [[Fascinated]] by their betrayer and unable to cease targeting them exclusively until the betrayer is defeated. <br>  <br> An ally can convince the revolutionary to forgo their vengeance with a DC 30 Diplomacy check to make a `act request dc=30`. This lasts for 1 minute, but talking the revolutionary down after that time requires more thorough engagement."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longsword +21 (`pf2:1`) (magical, versatile p), **Damage** 2d8+10 slashing"
  - name: "Melee strike"
    desc: "Fist +20 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+10 bludgeoning"
  - name: "Ranged strike"
    desc: "Composite Longbow +21 (`pf2:1`) (deadly d10, magical, propulsive, reload 0, volley 30, range 100 ft.), **Damage** 1d8+8 piercing"
spellcasting: []
abilities_bot:
  - name: "Darting Feint"
    desc: "`pf2:2` The exiled revolutionary Feints, Steps, and Strikes in any order."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Forces hire an exiled revolutionary because they were once part of the enemy. A lost scion, noble who spoke against tyranny, or wrongly persecuted politician possesses an intimate knowledge of their foe's tactics, logistics, and territory.

Whether they're hired to wage war, protect a caravan, or infiltrate an impenetrable fortress, there's ample work for mercenaries all over Golarion.

```statblock
creature: "Exiled Revolutionary"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
