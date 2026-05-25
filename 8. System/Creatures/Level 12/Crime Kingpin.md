---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Crime Kingpin"
level: "12"
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
    desc: "+22"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +25, Deception +24, Diplomacy +22, Intimidation +28, Society +24, Stealth +23, Thievery +24, Underworld Lore +24"
abilityMods: ["+3", "+5", "+3", "+2", "+2", "+6"]
abilities_top:
  - name: "+2 to Sense Motive"
    desc: ""
  - name: "Sneak Attack"
    desc: "The crime kingpin deals an additional 3d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "32; **Fort** +23, **Ref** +23, **Will** +22"
health:
  - name: HP
    desc: "250"
abilities_mid:
  - name: "Deny Advantage"
    desc: "The crime kingpin isn't [[Off Guard]] to creatures of 12th level or lower that are [[Hidden]], [[Undetected]], flanking, or using [[Surprise Attack]]."
  - name: "Kingpin's Presence"
    desc: "30 feet. <br>  <br> Allies in the aura gain a +2 status bonus to saving throws against mental effects."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "You'll Pay for That"
    desc: "`pf2:r` **Trigger** An enemy damages the kingpin <br>  <br> **Effect** The kingpin issues a vendetta against the enemy. Each of the kingpin's allies who hears the command gains a +5 status bonus to their next damage roll against that enemy. <br>  <br> > [!danger] Effect: You'll Pay for That"
  - name: "Kick Away"
    desc: "`pf2:r` **Trigger** The kingpin knocks an item out of a creature's grasp using [[Disarm]] <br>  <br> **Effect** The kingpin kicks the weapon up to 20 feet in any direction. If the kingpin kicks the weapon into an ally's square, that ally can catch the weapon as a free action, Releasing anything else they're holding if necessary."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Rapier +26 (`pf2:1`) (deadly d8, disarm, finesse, magical), **Damage** 2d6+11 piercing"
  - name: "Melee strike"
    desc: "Fist +26 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+11 bludgeoning"
  - name: "Ranged strike"
    desc: "Hand Crossbow +26 (`pf2:1`) (magical, reload 1, range 60 ft.), **Damage** 2d6+8 piercing"
spellcasting: []
abilities_bot:
  - name: "Fencing Brawl"
    desc: "`pf2:2` The kingpin attempts a rapier Strike followed by a `act disarm` or `act grapple` attempt against the same enemy. These count as one attack for the kingpin's multiple attack penalty, and the penalty doesn't increase until after both attacks."
  - name: "Kingpin's Command"
    desc: "`pf2:1` The crime kingpin shouts a command to an ally of their choice. That ally can spend a reaction to Stride and Strike. The ally becomes immune to Kingpin's Command for 24 hours."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Kingpins build empires from the shadows, ruling their territory ruthlessly and keeping their business private. Most forge connections with the rich and powerful, doing dirty work for politicians and minor nobles in return for influence and favors that can be called in at any time.

In the underbelly of society, the lawless reign supreme.

```statblock
creature: "Crime Kingpin"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
