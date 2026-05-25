---
type: creature
group: ["Undead", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Nosferatu Malefactor"
level: "10"
rare_01: "Uncommon"
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
    desc: "+19; [[Darkvision]]"
languages: "Aklo, Common, Necril (Telepathy 60 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +21, Arcana +21, Athletics +19, Deception +17, Intimidation +19, Stealth +23"
abilityMods: ["+5", "+7", "+3", "+7", "+5", "+3"]
abilities_top:
  - name: "Telepathy 60 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Nosferatu Vulnerabilities"
    desc: "- **Revulsion** A nosferatu can't voluntarily come within 10 feet of brandished garlic or a brandished religious symbol of a deity with a holy sanctification option. To brandish garlic or a religious symbol, a creature must Interact to do so for 1 round (similar to Raising a Shield). If the nosferatu involuntarily comes within 10 feet of an object of their revulsion, they gain the [[Fleeing]] condition, running from the object of their revulsion until they end an action beyond 10 feet. After 1 round of being exposed to the subject of their revulsion, a nosferatu can attempt a DC 25 [[Will]] save as a single action, which has the concentrate trait. On a success, they overcome their revulsions for 1d6 rounds (or 1 hour on a critical success). <br> - **Stake** A magical wooden stake (such as one affected by a weapon *potency rune*, [[Runic Weapon]], or similar magic) driven through the nosferatu's heart drops the nosferatu to 0 HP and prevents them from healing above 0 HP, even in their coffin. Staking a nosferatu requires 3 actions and works only if the nosferatu is [[Unconscious]]. If the stake is removed, the nosferatu can heal above 0 HP again, and if they're in their coffin, the 1-hour rest period begins once the stake is removed. If the nosferatu's head is severed and anointed with [[Holy Water]] while the stake is in place, the nosferatu is destroyed. <br> - **Sunlight** If exposed to direct sunlight, a nosferatu immediately becomes [[Slowed]] 1. The slowed value increases by 1 each time the nosferatu ends their turn in sunlight, and the condition ends when they're no longer in sunlight. If the nosferatu loses all their actions in this way, they're destroyed."
  - name: "Plague of Ancients"
    desc: "**Saving Throw** DC 29 [[Fortitude]] save <br>  <br> **Onset** 1 day <br>  <br> **Stage 1** [[Drained]] 1 (1 day) <br>  <br> **Stage 2** [[Drained]] 2 and [[Enfeebled]] 2 (1 day) <br>  <br> **Stage 3** [[Doomed]] 1, [[Drained]] 3, and [[Enfeebled]] 3 (1 day) <br>  <br> **Stage 4** [[Doomed]] 2, drained 3, and enfeebled 3 (1 day) <br>  <br> **Stage 5** [[Unconscious]] (1 day) <br>  <br> **Stage 6** death"
  - name: "Plagued Coffin Restoration"
    desc: "Unlike other undead, a nosferatu isn't destroyed at 0 HP. Instead, they disperse into an immense number of rats heading in every direction in an attempt to return to their coffin. If even a single rat reaches the coffin, the nosferatu can recover. A nosferatu regains their strength through resting in earth taken from the grave of a creature that died of plague. If their body rests in their earth-filled coffin for 1 hour, the nosferatu gains 1 HP, after which their fast healing begins to function normally. If the coffin doesn't contain this plagued grave dirt, they instead need to rest in their coffin for 1 day before they gain 1 HP and regain their fast healing."
armorclass:
  - name: AC
    desc: "30; **Fort** +17, **Ref** +21, **Will** +19"
health:
  - name: HP
    desc: "135; **Immunities** death effects, disease, paralyzed, poison, sleep"
abilities_mid:
  - name: "Fast Healing 10"
    desc: "A monster with this ability regains the given number of Hit Points each round at the beginning of its turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +23 (`pf2:1`) (agile, finesse), **Damage** 2d10+11 piercing plus [[Vampire Nosferatu Plague Of Ancients]]"
  - name: "Melee strike"
    desc: "Fangs +23 (`pf2:1`) (finesse), **Damage** 2d12+11 piercing plus [[Vampire Nosferatu Drink Blood]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 29, attack +21<br>**6th** [[Dominate (At-Will)]]<br>**5th** [[Telekinetic Haul]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The nosferatu transforms into a swarm of pale-gray rats. They gain a land Speed of 30 feet and a climb Speed of 10 feet, and they become Large. In this swarm form, the nosferatu can take an action to deal each enemy in the swarm's space @Damage[2d10[piercing]|options:area-damage] damage with a [[Reflex]] save. A creature that fails its save is also exposed to plague of ancients. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Command Thrall"
    desc: "`pf2:0` **Requirements** One of the nosferatu's thralls is present and can hear the nosferatu <br>  <br> **Effect** The nosferatu gives a single command to one of their thralls, which the thrall follows to the best of its ability during its next turn."
  - name: "Dominate"
    desc: "`pf2:2` The nosferatu can cast [[Dominate]] at will as a divine innate spell. Casting it requires staring into the target's eyes, giving the spell the visual trait. The save DC uses a high DC for the nosferatu's level, and a creature that succeeds is temporarily immune to that nosferatu's Dominate for 24 hours. Fully destroying the nosferatu ends the domination, but merely reducing the nosferatu to 0 HP is insufficient to break the spell."
  - name: "Drink Blood"
    desc: "`pf2:1` **Requirements** The nosferatu's last action was a successful fangs Strike <br>  <br> **Effect** The nosferatu sinks their fangs into the targeted creature to drink its blood. This requires an [[Athletics]] check against the creature's Fortitude DC. On a success, the creature becomes [[Drained]] 1, and the nosferatu regains 13 HP, gaining any excess HP as temporary Hit Points. Drinking Blood from a creature that's already drained doesn't restore any HP to the nosferatu but increases the creature's drained condition value by 1, killing the victim when it reaches [[Drained]] 5. A nosferatu can also consume blood that's been emptied into a vessel for sustenance, but they gain no HP from doing so. <br>  <br> The target creature's drained condition value decreases by 1 per week. A blood transfusion, which requires a successful DC 20 [[Medicine]] check and sufficient blood or a blood donor, reduces the drained value by 1 after 10 minutes."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Nosferatu malefactors spread plague in their wake and yearn for mortal blood.

Nosferatus are ancient vampires born of mortals who died in great plagues of old. Perhaps because of their old age, nosferatus can't create more of their kind.

```statblock
creature: "Nosferatu Malefactor"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
