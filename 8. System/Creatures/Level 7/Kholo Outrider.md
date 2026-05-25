---
type: creature
group: ["Humanoid", "Kholo"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Kholo Outrider"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Kholo"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Low-Light Vision]]"
languages: "Common, Kholo"
skills:
  - name: Skills
    desc: "Acrobatics +13, Athletics +18, Intimidation +13, Stealth +15, Survival +18"
abilityMods: ["+4", "+3", "+2", "+1", "+3", "+0"]
abilities_top:
  - name: "Rugged Travel"
    desc: "A kholo ignores the first square of difficult terrain they move into each time they Step or Stride."
  - name: "Solo Hunter"
    desc: "A kholo outrider deals 1d6 extra damage while adjacent to at least 2 enemies and no allies."
armorclass:
  - name: AC
    desc: "25; **Fort** +14, **Ref** +18, **Will** +13"
health:
  - name: HP
    desc: "120"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Hatchet +19 (`pf2:1`) (agile, magical, sweep), **Damage** 1d6+7 slashing"
  - name: "Melee strike"
    desc: "Hatchet +17 (`pf2:1`) (agile, magical, sweep, thrown 10), **Damage** 1d6+7 slashing"
  - name: "Melee strike"
    desc: "Jaws +18 (`pf2:1`) (unarmed), **Damage** 1d6+7 piercing"
  - name: "Ranged strike"
    desc: "Composite Shortbow +17 (`pf2:1`) (deadly d10, magical, propulsive, reload 0, range 60 ft.), **Damage** 1d6+5 piercing"
spellcasting: []
abilities_bot:
  - name: "Bloody Flurry"
    desc: "`pf2:2` The kholo outrider Strikes, Steps, then Strikes again. If the kholo outrider hits the same enemy with both Strikes, that enemy takes an additional 1d6 persistent,bleed damage."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Many kholo packs are semi-nomadic, staying in one place until they're pushed out by others, or the local resources begin to grow sparse. Before moving the pack elsewhere, the leaders send out a single kholo to blaze a trail and ensure a safe route to their next destination. These outriders are masters of the wilderness and fight better when they're alone.

These pragmatic hunters have earned a very poor reputation for their brutality in battle and worship of demons. While many kholos live up to the terrible stories of their ferocity and cannibalism, others are scavengers and trappers just trying to get by. Many of their cultural traditions are misunderstood by other ancestries, and some kholos play into the fear provoked in those who believe the twisted tales about their people. Kholos are often criticized for their lack of honor in battle, but a kholo understands honor doesn't bring you back home alive, nor does honor put food on the table. Ambushes, feints, and deceptions that lead to fewer kholo deaths and a quicker victory are simply the logical thing to do.

```statblock
creature: "Kholo Outrider"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
