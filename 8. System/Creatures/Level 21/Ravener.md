---
type: creature
group: ["Dragon", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ravener"
level: "21"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Dragon"
trait_02: "Fire"
trait_03: "Primal"
trait_04: "Undead"
trait_05: "Unholy"
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+37; [[Darkvision]], [[Scent]] (imprecise) 60 feet"
languages: "Common, Draconic, Necril, Pyric"
skills:
  - name: Skills
    desc: "Acrobatics +32, Athletics +39, Deception +38, Diplomacy +38, Intimidation +40, Nature +32, Stealth +35"
abilityMods: ["+9", "+5", "+9", "+5", "+6", "+8"]
abilities_top:
  - name: "Smoke Vision"
    desc: "Smoke doesn't impair a cinder ravener's vision; it ignores the [[Concealed]] condition from smoke."
  - name: "Soulsense 60 feet"
    desc: "A ravener senses the spiritual essence of living and undead creatures within the listed range. Creatures whose material bodies are one unit with their souls, like celestials and fiends, appear brighter to this sense."
  - name: "Vicious Criticals"
    desc: "The ravener treats an attack roll as a critical hit on a roll of 19 or 20, as long as the attack roll was a success. Additionally, whenever the ravener makes a critical hit with one of their Strikes, the target must succeed on a DC 42 [[Fortitude]] save or gain the [[Drained]] 1 condition. If the target already has a drained value of greater than 0, their drained value instead increases by 1, to a maximum of drained 4. Whenever the ravener applies drain to a creature in this way, their soul ward gains 5 Hit Points."
armorclass:
  - name: AC
    desc: "47; **Fort** +38, **Ref** +34, **Will** +37"
health:
  - name: HP
    desc: "500; **Immunities** bleed, death effects, disease, fire, paralyzed, poison, sleep; **Weaknesses** cold 20, holy 20"
abilities_mid:
  - name: "+2 Status to All Saves vs. Primal"
    desc: ""
  - name: "Cowering Fear"
    desc: "90 feet. DC 42 [[Will]] save <br>  <br> A ravener's frightful presence causes creatures to cower in fear as well. As long as a creature is at least [[Frightened]] 2 or more as a result of the ravener's frightful presence, it's also [[Immobilized]] from the fear. <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Discorporate"
    desc: "`pf2:0` **Trigger** The ravener takes excess damage to their soul ward but still has at least 51 Hit Points in their soul ward <br>  <br> **Effect** The ravener draws deeply into their soul ward, discorporating their body into soul energy to escape. They take 50 untyped damage to their soul ward and their physical body vanishes, reappearing 1d4 hours later in a random location within 1 mile from the location where they used Discorporate."
  - name: "Reactive Strike (Jaws Only)"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Soul Ward"
    desc: "200 HP <br>  <br> An intangible field of necromantic energy protects a ravener from total destruction. A soul ward has 150 maximum Hit Points, or 200 if the ravener is level 21 or higher. Whenever a ravener would be reduced below 1 Hit Point, all damage in excess of what would reduce them to 1 Hit Point is instead dealt to their soul ward. If this damage reduces the soul ward to fewer than 0 Hit Points, the ravener is destroyed. A soul ward's Hit Points can be restored only via specific ravener abilities such as Consume Soul, Void Breath, or vicious criticals. A ravener who goes more than a week without successfully using Consume Soul to feed on a dying creature starves, and their soul ward loses 1d4 Hit Points each day until they feed. If the ravener's soul ward loses all its Hit Points while the ravener still has more than 1 HP, they become a ravener husk."
  - name: "Consume Soul"
    desc: "`pf2:0` **Trigger** A living creature within 30 feet of the ravener dies <br>  <br> **Effect** The ravener tears the creature's soul from its body with their maw and gulps it down. The dying creature must attempt a DC 44 [[Fortitude]] save with the same DC as the ravener's breath ability. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The ravener tears off a small chunk of the creature's soul. If the victim is restored to life, they are [[Drained]] 1 in addition to any other side effects of returning to life. The ravener adds a number of Hit Points to their soul ward equal to half the creature's level. <br> - **Failure** As success, but the creature's soul is ravaged. The creature is [[Drained]] 3 and the ravener adds a number of Hit Points to their soul ward equal to the creature's level. <br> - **Critical Failure** As failure, but the ravener devours the entire soul. The victim can't be restored to life as long as the ravener exists except via powerful magic such as a wish ritual, and the ravener adds a number of Hit Points to their soul ward equal to twice the creature's level."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +39 (`pf2:1`) (fire, magical, reach 20 ft.), **Damage** 4d12+13 piercing plus 2d6 fire plus 2d6 void"
  - name: "Melee strike"
    desc: "Horn +37 (`pf2:1`) (magical, reach 20 ft.), **Damage** 2d6 void plus 4d12+17 slashing"
  - name: "Melee strike"
    desc: "Claw +39 (`pf2:1`) (agile, magical, reach 15 ft.), **Damage** 4d10+13 slashing plus 2d6 void"
  - name: "Melee strike"
    desc: "Tail +37 (`pf2:1`) (magical, reach 25 ft.), **Damage** 4d8+13 slashing plus 2d6 void"
  - name: "Melee strike"
    desc: "Wing +37 (`pf2:1`) (agile, magical, reach 20 ft.), **Damage** 4d8+13 slashing plus 2d6 void"
spellcasting: []
abilities_bot:
  - name: "All Becomes Flame"
    desc: "`pf2:1` The ravener curses a creature within 60 feet to have their magic replaced with primordial flames. The creature must attempt a DC 42 [[Will]] save. Regardless of the result, the target becomes temporarily immune for 1 day. Critical Success The creature is unaffected. <br> - **Success** The creature is cursed for 1 round. While cursed, any spells that the creature casts gain the fire trait and have their damage type changed to fire damage, regardless of the original damage type or types of the spell. Additionally, any magical items that the cursed target holds or wields are affected in the same manner, such as changing the cold damage of a frost rune to fire damage. The cursed creature can attempt to temporarily suppress the curse as an action, which has the concentrate trait. If the creature succeeds a DC 42 [[Will]] save, the curse is suppressed until the end of their turn. <br> - **Failure** As success, but the curse's duration is 1 hour. <br> - **Critical Failure** As success, but the curse's duration is 1 day, and the DC to suppress the curse increases to DC 44."
  - name: "Manipulate Flames"
    desc: "`pf2:1` The ravener intensifies nearby fires. Every foe within 60 feet taking persistent fire damage takes 5d6 fire damage."
  - name: "Void Breath"
    desc: "`pf2:2` The ravener breathes a blast of necrotic flame that deals 20d6 fire damage plus 4d6 persistent,void damage (DC 44 [[Reflex]] save). A creature that fails its save is also [[Drained]] 1 (or [[Drained]] 2 on a critical failure). If a creature is drained by the ravener's Void Breath, the ravener's soul ward gains 5 HP. The ravener can't use Void Breath again for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The ravener presented here was once an ancient cinder dragon.

Though their lifespans can measure in millennia, all dragons must eventually perish. While many do so on the blades or under the spells of dragonslayers, some manage to outlast their enemies and must, in time, face the truth that awaits all living creatures at the end of their natural life span. As with many other creatures, some dragons respond to such looming reminders of their own mortality poorly, and the particularly prideful or wrathful of their kind often lash out in anger when confronted by this grim truth. Peace and acceptance are found by some dragons, but the most stubborn of their ilk (and invariably the most wicked) can pursue a different answer to the problem. These dragons seek out sinister rites that can transform them into undead creatures known as raveners.

A ravener's flesh is stripped away as part of the transformation, leaving only bones. What they lose in flesh, however, the dragon gains in soul-rending power, as their spiritual energy forms a protective barrier around their body, keeping it intact and allowing flight with now-skeletal wings. This existence isn't as easy to maintain as other forms of undeath, however, and the ravener must feed regularly on living souls to power their profane metabolism. Their hunger is much greater than that of a living dragon, so raveners are forced to relocate regularly, traveling to fresh hunting grounds each time they strip their current home of prey.

```statblock
creature: "Ravener"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
