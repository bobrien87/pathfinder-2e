---
type: creature
group: ["Undead", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Vampire Servitor"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Undead"
trait_02: "Unholy"
trait_03: "Vampire"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Darkvision]]"
languages: "Common (plus one regional language)"
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +9, Intimidation +8, Society +5, Stealth +12"
abilityMods: ["+3", "+5", "+1", "-1", "+3", "+2"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The servitor deals 1d6 extra precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "22; **Fort** +9, **Ref** +13, **Will** +11"
health:
  - name: HP
    desc: "40; coffin restoration, fast healing 5, void healing; **Immunities** death effects, disease, paralyzed, poison, sleep; **Resistances** physical 5 except silver"
abilities_mid:
  - name: "Fast Healing 5"
    desc: "A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
  - name: "Coffin Restoration"
    desc: "Unlike other undead, a vampire isn't destroyed at 0 HP. Instead, it falls [[Unconscious]]. If its body rests in its coffin for 1 hour, the vampire gains 1 HP, after which its fast healing begins to function normally."
  - name: "Vampire Vulnerabilities"
    desc: "All vampires possess the following vulnerabilities. <br>  <br> - **Compulsions** Vampires are creatures with strange and unknowable compulsions. A typical vampire can't voluntarily cross running water unless they're transported while they hide within their coffin, nor can they enter a private dwelling unless invited in by someone with the authority to do so. At your discretion, vampires might have different compulsions—a pirate vampire might not be able to set foot on solid ground without being invited, for example. The vampire can still be forced to do these things and might be able to overcome their compulsion just as they do their revulsion. <br>  <br> - **Revulsion** A vampire can't voluntarily come within 10 feet of brandished garlic or a brandished religious symbol of a deity with a holy sanctification option. To brandish garlic or a religious symbol, a creature must Interact to do so, and it remains brandished for 1 round (similar to Raising a Shield). If the vampire involuntarily comes within 10 feet of an object of their revulsion, they gain the [[Fleeing]] condition, running from the object of their revulsion until they end an action beyond 10 feet. After 1 round of being exposed to the subject of their revulsion, a vampire can attempt a DC 25 [[Will]] save as a single action, which has the concentrate trait. On a success, they overcome their revulsions for 1d6 rounds (or 1 hour on a critical success). <br>  <br> - **Stake** A wooden stake driven through a vampire's heart drops the vampire to 0 HP and prevents them from healing above 0 HP, even in their coffin. Staking a vampire requires 3 actions and works only if the vampire is [[Unconscious]]. If the stake is removed, the vampire can heal above 0 HP again, and if they're in their coffin, the 1-hour rest period begins once the stake is removed. If the vampire's head is severed and anointed with holy water while the stake is in place, the vampire is destroyed. <br>  <br> - **Sunlight** If exposed to direct sunlight, a vampire immediately becomes [[Slowed]] 1. The slowed value increases by 1 each time the vampire ends their turn in sunlight, and the condition ends when they're no longer in sunlight. If the vampire loses all their actions in this way, they're destroyed. Due to their supernatural aversion to light, vampires don't cast shadows or show a reflection in mirrors"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +14 (`pf2:1`) (agile, unarmed), **Damage** 1d8+6 slashing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Drink Blood"
    desc: "`pf2:1` **Requirement** A [[Grabbed]], [[Paralyzed]], [[Restrained]], [[Unconscious]], or willing creature is within the vampire's reach. <br>  <br> **Effect** The vampire sinks its fangs into that creature to drink its blood. This requires an [[Athletics]] check against the victim's Fortitude DC if the victim is grabbed and is automatic for any of the other conditions. <br>  <br> The victim is [[Drained]] 1 and the vampire regains 5 HP, gaining any excess HP as temporary Hit Points. Drinking Blood from a creature that's already drained doesn't restore any HP to the vampire but increases the victim's drained value by 1, killing the victim when it reaches drained 5. A vampire can also consume blood that's been emptied into a vessel for sustenance, but it gains no HP from doing so. <br>  <br> A victim's drained condition decreases by 1 per week. A blood transfusion, which requires a DC 20 [[Medicine]] check and sufficient blood or a blood donor, reduces the drain by 1 after 10 minutes."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Vampires use their servitor pawns for infiltration and reconnaissance.

Vampires are undead creatures that feed on the blood of the living.

```statblock
creature: "Vampire Servitor"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
